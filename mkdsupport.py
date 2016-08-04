"""An Sphinx extension supporting for sphinx.ext.autodoc with modules containing docstrings in Markdown
"""

import pypandoc


def setup(app):
    app.add_config_value('mkdsupport_use_parser', 'markdown', True)
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
