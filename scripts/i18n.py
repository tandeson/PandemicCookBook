#!/usr/bin/env python
#*****************************************************************************
#
"""
    Minimal localization helpers for cookbook output.
"""
#
#*****************************************************************************

LANGUAGE_PACKS = {
    'en': {
        'language_name': 'English',
        'labels': {
            'html_lang': 'en',
            'html_font_family': '"Palatino Linotype", "Book Antiqua", Palatino, serif',
            'recipe_kicker': 'Recipe',
            'ingredients': 'Ingredients',
            'steps': 'Steps',
            'notes': 'Notes',
            'instructions': 'Instructions',
            'directions': 'Directions',
            'recipes': 'Recipes',
            'recipe_list': 'Recipe List',
            'ingredients_list': 'Ingredients List',
            'empty_directories': 'Empty Directories',
            'todo': 'TODO',
            'index': 'Index',
            'by_ingredient': 'By Ingredient',
            'title': 'The Pandemic Cookbook',
            'copyright': 'Copyright',
            'by': 'by',
            'all_rights_reserved': 'All Rights Reserved.',
            'published_by': 'Published by Lulu Press',
            'git_info': 'Git Info',
            'commit': 'Commit',
            'clean_commit': 'Clean Commit',
            'template': 'Template',
            'generated': 'Generated',
            'using_tool': 'using tool',
            'version': 'version',
            'page_abbrev': 'pg',
            'intro': (
                "The following are the things we've been cooking together as we find ways to "
                "keep busy inside and away from people. We've been enjoying them, and we hope you do too."
            ),
        },
        'latex': {
            'compiler': None,
            'use_polyglossia': False,
            'main_font': None,
            'language': 'english',
            'passes': 1,
        },
    },
    'bg': {
        'language_name': 'Bulgarian',
        'labels': {
            'html_lang': 'bg',
            'html_font_family': '"Times New Roman", "DejaVu Serif", "Liberation Serif", serif',
            'recipe_kicker': 'Рецепта',
            'ingredients': 'Съставки',
            'steps': 'Стъпки',
            'notes': 'Бележки',
            'instructions': 'Инструкции',
            'directions': 'Приготвяне',
            'recipes': 'Рецепти',
            'recipe_list': 'Списък с рецепти',
            'ingredients_list': 'Списък със съставки',
            'empty_directories': 'Празни директории',
            'todo': 'ЗА ВЪРШЕНЕ',
            'index': 'Индекс',
            'by_ingredient': 'По съставка',
            'title': 'Пандемичната готварска книга',
            'copyright': 'Авторско право',
            'by': 'от',
            'all_rights_reserved': 'Всички права запазени.',
            'published_by': 'Издател: Lulu Press',
            'git_info': 'Git информация',
            'commit': 'Комит',
            'clean_commit': 'Чист комит',
            'template': 'Шаблон',
            'generated': 'Генерирано',
            'using_tool': 'с инструмент',
            'version': 'версия',
            'page_abbrev': 'стр.',
            'intro': (
                'Следват нещата, които готвим заедно, докато търсим начини да '
                'остаем заети вкъщи и далеч от хората. Наслаждаваме им се и се '
                'надяваме и на вас да ви харесат.'
            ),
        },
        'latex': {
            'compiler': 'xelatex',
            'use_polyglossia': True,
            'main_font': 'DejaVu Serif',
            'language': 'bulgarian',
            'passes': 2,
        },
    },
}


def get_language_pack(lang_code):
    """
    Return a language pack with labels and renderer settings.
    """
    if not lang_code:
        return LANGUAGE_PACKS['en']
    return LANGUAGE_PACKS.get(lang_code.lower(), LANGUAGE_PACKS['en'])
