---
Sphinx Markdown Extension
---

An Sphinx extension supporting for sphinx.ext.autodoc with modules containing docstrings in Markdown.

# How it works

This extension reads your docstrings in ```Markdown```, and translates it to ```reStructuredText``` using ```pandoc```, so that Sphinx can deal with it. This only processes docstrings and it doesn't do anything to any other files which Sphinx reads. So, for example, if you have an ```index.rst```, that file still needs to be written in ReStructuredText.

# How to use it

## Requirements

* Python 3.4 or 3.5 since ```pypandoc``` only supports Python 2.7, 3.4 and 3.5.

* pypandoc (install it by ```pip install pypandoc``` in ```cmd```)

## Usage

The default input format is GitHub-Flavored Markdown and you can change it to other format as long as [Pandoc](http://pandoc.org/MANUAL.html) can support. For this, you need to change the ```mkdsupport_use_parser``` from ```markdown_github``` to the format you want in the extension source file ```mkdsupport.py```.

Put this extension ```mkdsupport.py``` into the directory containing ```conf.py``` file which is also the root of your Sphinx project.

Add the following code to ```conf.py``` file to set module search path ```sys.path``` of Python so that Sphinx can find the extension. 

```python
import sys
import os

sys.path.append(0, os.path.abspath('.'))
```

Add ```mkdsupport``` to ```conf.py``` file so that this extension is enabled as following.

```python
extensions = ['mkdsupport']
```

# Reminder

- Actually you can put this extension to directory you want and put this directory to the ```sys.path```. However, the Sphinx project directory is suggested since the extension is not official. In this way, there is no pollution on Sphinx installation directory and it is easier for managing the settings.

- If you change the input format, such as the default one ```markdown_github```, in this extension and there are no changes in your project source files, this extension will not be triggered and there are no updating in your generated documentation.

# References

- [Sphinx Extensions](http://www.sphinx-doc.org/en/stable/extensions.html#builtin-sphinx-extensions)

- [Tutorial: Writing a simple extension](http://www.sphinx-doc.org/en/stable/extdev/tutorial.html#the-setup-function)

- [Sphinx.add_config_value(name, default, rebuild)](http://www.sphinx-doc.org/en/stable/extdev/appapi.html#sphinx.application.Sphinx.add_config_value)

- [Sphinx.connect(event, callback)](http://www.sphinx-doc.org/en/stable/extdev/appapi.html#sphinx.application.Sphinx.connect)

- [autodoc-process-docstring(app, what, name, obj, options, lines)](http://www.sphinx-doc.org/en/stable/ext/autodoc.html?highlight=autodoc-process-docstring#event-autodoc-process-docstring)

- [source_encoding](http://www.sphinx-doc.org/en/stable/config.html)

- [pypandoc](https://github.com/bebraw/pypandoc)