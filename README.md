[![Pylint](https://github.com/gaspardpetit/uniscripts/actions/workflows/pylint.yml/badge.svg)](https://github.com/gaspardpetit/uniscripts/actions/workflows/pylint.yml)
[![Python package](https://github.com/gaspardpetit/uniscripts/actions/workflows/python-package.yml/badge.svg)](https://github.com/gaspardpetit/uniscripts/actions/workflows/python-package.yml)
[![PyPI version](https://badge.fury.io/py/uniscripts.svg)](https://pypi.python.org/pypi/uniscripts/)
[![Python versions](https://img.shields.io/pypi/pyversions/uniscripts.svg)](https://pypi.org/project/uniscripts/)
[![Unicode versions](https://img.shields.io/badge/Unicode%20-15.1-blue.svg)](https://www.unicode.org/charts/)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)

# Uniscripts

Simple Python 3 module to query Unicode UCD script metadata (see UAX #24).

This module is useful for querying if a text is made of Latin characters,
Arabic, hiragana, kanji (han), and so on.  It works for all scripts supported
by the Unicode character database.

Sample usage:

```python
>>> from uniscripts import is_script, which_scripts, Scripts

>>> is_script('A', Scripts.LATIN)
True

# if you pass it a string, all characters must match
>>> is_script('はるはあけぼの', Scripts.HIRAGANA)
True

>>> is_script('はるはAkebono', Scripts.HIRAGANA)
False

# ...but by default, it ignores 'Common' characters, such as punctuation.
>>> is_script('はるは:あけぼの', Scripts.HIRAGANA)
True

>>> is_script('中華人民共和国', Scripts.HAN) # 'Han' = kanji or hànzì
True

>>> which_scripts('z')
['Latin']

>>> which_scripts('は')
['Hiragana']

>>> which_scripts('ー') # U+30FC
['Bopomofo', 'Common', 'Han', 'Hangul', 'Hiragana', 'Katakana', 'Yi']

See docstrings for `is_script()`, `which_scripts()`.
