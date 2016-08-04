---
Sphinx Markdown Extension
---

An Sphinx extension supporting for sphinx.ext.autodoc with modules containing docstrings in Markdown.

# How it works

This extension reads your docstrings in ```Markdown```, and translates it to ```reStructuredText``` using ```pandoc```, so that Sphinx can deal with it. This only processes docstrings and it doesn't do anything to any other files which Sphinx reads. So, for example, if you have an ```index.rst```, that file still needs to be written in ReStructuredText.

# How to use it

- Put this extension ```mkdsupport.py``` into the directory containing ```conf.py`` file which is also the root of your Sphinx project.

- Set module search path ```sys.path``` of Python so that Sphinx can find the extension. Add the following code to ```conf.py``` file:

```python
import sys
import os
sys.path.append(0, os.path.abspath('.'))
```

**Note:** Actually you can put this extension to directory you want and put this directory to the ```sys.path```. However, the Sphinx project directory is suggested since the extension is not official. In this way, there is no pollution on Sphinx installation directory and it is easier to manage the settings.

- Add ```mkdsupport``` to ```conf.py``` file so that this extension is enabled.

# References

- [Sphinx Extensions](http://www.sphinx-doc.org/en/stable/extensions.html#builtin-sphinx-extensions)

- [Tutorial: Writing a simple extension](http://www.sphinx-doc.org/en/stable/extdev/tutorial.html#the-setup-function)

- [Sphinx.add_config_value(name, default, rebuild)](http://www.sphinx-doc.org/en/stable/extdev/appapi.html#sphinx.application.Sphinx.add_config_value)

- [Sphinx.connect(event, callback)](http://www.sphinx-doc.org/en/stable/extdev/appapi.html#sphinx.application.Sphinx.connect)

- [autodoc-process-docstring(app, what, name, obj, options, lines)](http://www.sphinx-doc.org/en/stable/ext/autodoc.html?highlight=autodoc-process-docstring#event-autodoc-process-docstring)

- [source_encoding](http://www.sphinx-doc.org/en/stable/config.html)

- [pypandoc](https://github.com/bebraw/pypandoc)