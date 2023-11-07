from __future__ import unicode_literals
from pybtex.style.formatting.unsrt import Style as UnsrtStyle
from pybtex.style.formatting import BaseStyle, toplevel
from pybtex.style.formatting.unsrt import pages, date
from pybtex.style.template import (
    field, first_of, href, join, names, optional, optional_field, sentence,
    tag, together, words
)
#from pybtex.style.template import toplevel # ... and anything else needed


from pybtex.style.sorting.author_year_title import SortingStyle

class MySortingStyle(SortingStyle):

    def sorting_key(self, entry):
        if entry.type in ('book', 'inbook'):
            author_key = self.author_editor_key(entry)
        elif 'author' in entry.persons:
            author_key = self.persons_key(entry.persons['author'])
        else:
            author_key = ''
        return (entry.fields.get('year', ''), author_key, entry.fields.get('title', ''))


import pybtex.plugin
pybtex.plugin.register_plugin('pybtex.style.sorting', 'year_author_title', MySortingStyle)

class MyStyle(UnsrtStyle):

    default_sorting_style = 'year_author_title'

    def get_article_template(self, e):
        volume_and_pages = first_of [
            # volume and pages, with optional issue number
            optional [
                join [
                    field('volume'),
                    optional['(', field('number'),')'],
                    ':', pages
                ],
            ],
            # pages only
            words ['pages', pages],
        ]
        template = toplevel [
            self.format_names('author'),
            self.format_title(e, 'title'),
            sentence [
                tag('strong') [field('journal')],
                optional[ volume_and_pages ],
                tag('strong') [date]],
            sentence [ optional_field('note') ],
            self.format_web_refs(e),
        ]
        return template
