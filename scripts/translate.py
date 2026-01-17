#!/usr/bin/env python
#*****************************************************************************
#
"""
    Translation helpers backed by OpenAI with local caching.
"""
#
#*****************************************************************************

import json
import os
import sys
import urllib.request
import urllib.error
from pathlib import Path


class OpenAITranslator:
    """
    Simple OpenAI-backed translator with persistent JSON cache.
    """
    def __init__(self, api_key, model, target_language, cache_path, refresh=False, timeout=45):
        self.api_key = api_key
        self.model = model
        self.target_language = target_language
        self.cache_path = Path(cache_path)
        self.refresh = refresh
        self.timeout = timeout
        self.cache = {}
        self._load_cache()

    def _load_cache(self):
        if not self.cache_path.exists():
            return
        try:
            with self.cache_path.open('r', encoding='utf-8') as handle:
                self.cache = json.load(handle)
        except Exception as exc:
            sys.stderr.write("Warning: could not read translation cache: %s\n" % exc)
            self.cache = {}

    def _save_cache(self):
        try:
            self.cache_path.parent.mkdir(parents=True, exist_ok=True)
            tmp_path = self.cache_path.with_suffix(self.cache_path.suffix + '.tmp')
            with tmp_path.open('w', encoding='utf-8') as handle:
                json.dump(self.cache, handle, ensure_ascii=False, indent=2)
            os.replace(tmp_path, self.cache_path)
        except Exception as exc:
            sys.stderr.write("Warning: could not write translation cache: %s\n" % exc)

    def translate(self, text):
        if text is None:
            return text
        if not str(text).strip():
            return text

        key = "%s::%s" % (self.target_language, text)
        if (not self.refresh) and key in self.cache:
            return self.cache[key]

        translated = self._call_openai(text)
        if translated:
            self.cache[key] = translated
            self._save_cache()
            return translated

        return text

    def _call_openai(self, text):
        url = "https://api.openai.com/v1/chat/completions"
        system_prompt = (
            "You are a translation engine. Translate user content from English to "
            "%s. Preserve meaning, formatting, punctuation, and quantities/units. "
            "Keep proper nouns where appropriate. Return only the translated text."
        ) % self.target_language

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text},
            ],
            "temperature": 0,
        }

        data = json.dumps(payload).encode('utf-8')
        request = urllib.request.Request(
            url,
            data=data,
            headers={
                "Authorization": "Bearer %s" % self.api_key,
                "Content-Type": "application/json",
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                body = response.read().decode('utf-8')
            parsed = json.loads(body)
            return parsed["choices"][0]["message"]["content"].strip()
        except urllib.error.HTTPError as exc:
            err_body = exc.read().decode('utf-8', errors='ignore')
            sys.stderr.write("Translation HTTP error: %s\n%s\n" % (exc, err_body))
        except Exception as exc:
            sys.stderr.write("Translation error: %s\n" % exc)

        return None


class LocalMapTranslator:
    """
    Simple translator that relies on a provided text-to-text mapping.
    """
    def __init__(self, mapping, target_language=None):
        self.mapping = dict(mapping or {})
        self.target_language = target_language

    def add_mapping(self, mapping):
        if mapping:
            self.mapping.update(mapping)

    def translate(self, text):
        if text is None:
            return text
        if not str(text).strip():
            return text
        return self.mapping.get(text, text)


class CompositeTranslator:
    """
    Try translators in order; first that changes the text wins.
    """
    def __init__(self, translators):
        self.translators = [translator for translator in translators if translator]

    def translate(self, text):
        if text is None:
            return text
        if not str(text).strip():
            return text
        for translator in self.translators:
            translated = translator.translate(text)
            if translated != text:
                return translated
        return text
