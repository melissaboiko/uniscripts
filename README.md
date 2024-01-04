Simple Python 3 module to query Unicode UCD script metadata (see UAX #24).

This module is useful for querying if a text is made of Latin characters,
Arabic, hiragana, kanji (han), and so on.  It works for all scripts supported
by the Unicode character database.

This module is dumb and slow.  If you need speed, you probably want to
implement your own functions.  See e.g. `man pcreunicode`, `man pcrepattern`
(`grep -P` supports `\p`).  As of this writing, the next-generation of Python
regexpes, available as the pypi library `regex`, also supports `\p`.

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
