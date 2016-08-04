---
Sphinx Markdown Extension
---

An Sphinx extension supporting for sphinx.ext.autodoc with modules containing docstrings in Markdown.

# How it works

This extension reads your docstrings in ```Markdown```, and translates it to ```reStructuredText``` using ```pandoc```, so that Sphinx can deal with it. This only processes docstrings and it doesn't do anything to any other files which Sphinx reads. So, for example, if you have an ```index.rst```, that file still needs to be written in ReStructuredText.

# How to use it

- Put this extension ```mkd2rst.py``` into the directory containing ```conf.py`` file which is also the root of your Sphinx project.

- Set module search path ```sys.path``` of Python so that Sphinx can find the extension. Add the following code to ```conf.py``` file:

```python
import sys
import os
sys.path.append(0, os.path.abspath('.'))
```

**Note:** Actually you can put this extension to directory you want and put this directory to the ```sys.path```. However, the Sphinx project directory is suggested since the extension is not official. In this way, there is no pollution on Sphinx installation directory and it is easier to manage the settings.

- Add ```mkd2rst``` to ```conf.py``` file so that this extension is enabled.

# References

[Sphinx Extensions](http://www.sphinx-doc.org/en/stable/extensions.html#builtin-sphinx-extensions)
