# Error Messages

## How do I resolve Unicode Errors?

A typical error message is:

```python
UnicodeEncodeError: 'ascii' codec can't encode character u'\xe1' in position 426: ordinal not in range(128)
```

All strings should be unicode. In Python 2.7, they have a `u` in front of the string, like `u"foo"`; in Python 3, all strings are unicode. If you are careful to make sure your data is unicode, you shouldn't have this problem. Also, unless you are reading this in 2019 or earlier, you should not be using Python 2.

You can specify the encoding of text in your python files as UTF-8 by putting the following as the *first line* in each file: `# -*- coding: utf-8 -*-`

