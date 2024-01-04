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
>>> import uniscripts

>>> uniscripts.is_script('A', 'Latin')
True

# if you pass it a string, all characters must match
>>> uniscripts.is_script('はるはあけぼの', 'Hiragana')
True

>>> uniscripts.is_script('はるはAkebono', 'Hiragana')
False

# ...but by default, it ignores 'Common' characters, such as punctuation.
>>> uniscripts.is_script('はるは:あけぼの', 'Hiragana')
True

>>> uniscripts.is_script('中華人民共和国', 'Han') # 'Han' = kanji or hànzì
True

>>> uniscripts.which_scripts('z')
['Latin']

>>> uniscripts.which_scripts('は')
['Hiragana']

>>> uniscripts.which_scripts('ー') # U+30FC
['Bopomofo', 'Common', 'Han', 'Hangul', 'Hiragana', 'Katakana', 'Yi']

See docstrings for `is_script()`, `which_scripts()`.
