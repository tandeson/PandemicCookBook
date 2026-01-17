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
    """
    Register a translator instance for runtime text translation.
    """
    global _TRANSLATOR
    _TRANSLATOR = translator


def translate_text(text):
    """
    Translate text if a translator is configured, otherwise return original.
    """
    if text is None:
        return text
    if _TRANSLATOR is None:
        return text
    return _TRANSLATOR.translate(text)
