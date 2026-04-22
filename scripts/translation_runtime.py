#!/usr/bin/env python
#*****************************************************************************
#
"""
    Runtime translation hooks shared across modules.
"""
#
#*****************************************************************************

_TRANSLATOR = None


def set_translator(translator):
    global _TRANSLATOR
    _TRANSLATOR = translator


def translate_text(text):
    if text is None:
        return text
    if _TRANSLATOR is None:
        return text
    return _TRANSLATOR.translate(text)


class LocalMapTranslator:
    """
    Translates text using a pre-built string-to-string mapping (from Bulgarian JSON files).
    Falls back to the original text for any string not in the map.
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
