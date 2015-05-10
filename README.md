Simple Python 3 module to access Unicode UCD script metadata (see UAX #24).

Sample usage:

    >>> import uniscripts
    >>> uniscripts.is_script('A', 'Latin')
    True

    >>> uniscripts.is_script('はるはあけぼの', 'Hiragana')
    True

    >>> uniscripts.which_scripts('z')
    ['Latin']

    >>> uniscripts.which_scripts('は')
    ['Hiragana']

    >>> uniscripts.which_scripts('ー') # U+30FC
    ['Common', 'Katakana', 'Hiragana', 'Hangul', 'Han', 'Bopomofo', 'Yi']

See docstrings for `is_script()`, `which_scripts()`.
