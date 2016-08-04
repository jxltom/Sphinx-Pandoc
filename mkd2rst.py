"""Pandoc extension for Sphinx

This allows you to write your docstrings in whatever markup you want, as long
as pandoc supports it. Markdown is used by default; use the pandoc_use_parser
config value to change it to something else.

To use, place the contents of this file in your conf.py. Alternately, put it
somewhere in your Python path (or add where it is to your Python path) and add
'pandoc' to the `extensions` value in your conf.py.
"""

import pypandoc

def setup(app):
    app.add_config_value('pandoc_use_parser', 'markdown', True)
    app.connect('autodoc-process-docstring', pandoc_process)

def pandoc_process(app, what, name, obj, options, lines):
    if not lines:
        return
    input_format = app.config.pandoc_use_parser
    data = '\n'.join(lines)
    data = data.encode('utf-8')
    data = unicode(pypandoc.convert(data, 'rst', format=input_format),
                   encoding='utf-8')
    # Sphinx expects `lines` to be edited in place, so we have to replace it
    # like this.
    new_lines = data.split('\n')
    del lines[:]
    lines.extend(new_lines)
