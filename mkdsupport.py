"""An Sphinx extension supporting for sphinx.ext.autodoc with modules containing docstrings in Markdown
"""

import pypandoc


def setup(app):
    """Add extension's default value and set new function to ```autodoc-process-docstring``` event
    """

    # The 'rebuild' parameter should set as 'html' rather than 'env' since this extension needs a full rebuild of HTML
    # document
    app.add_config_value('mkdsupport_use_parser', 'markdown', 'html')
    app.connect('autodoc-process-docstring', pandoc_process)


def pandoc_process(app, what, name, obj, options, lines):
    """"Convert docstrings in Markdown into reStructureText using pandoc
    """

    if not lines:
        return None

    input_format = app.config.mkdsupport_use_parser
    output_format = 'rst'

    # Since pypandoc.convert_text, which will always return a unicode string, expects unicode or utf-8 encodes string
    # and the default encoding for Sphinx is 'utf-8-sig', it is better to convert to'utf-8' to Pandoc and then convert
    # it back after processed
    text = '\n'.join(lines).encode('utf-8')
    text = pypandoc.convert_text(text, output_format, format=input_format).encode('utf-8')

    # The 'lines' in Sphinx is a list of strings
    del lines[:]
    lines.extend(text.split('\n'))
