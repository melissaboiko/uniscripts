'''
Python interface to query Unicode UCD script data (UAX #24).

Tests whether a character belongs to a script, and so on.
'''

__version__ = "1.0.5"

from uniscripts.unidata import BUCKETS, SCRIPT_ABBREVS

# pylint: disable=dangerous-default-value
def is_script(string, script, ignore=['Inherited', 'Common', 'Unknown']):
    """Returns: true if all chars in string belong to script.

    Args:
        string: A string to test (may be a single char).
        script: Script long name, as in Unicode UCD's Scripts.txt (viz.).
        ignore: A list of scripts that will always suceed for matching purposes.
            For example, ASCII punctuation is listed as 'Common', so 'A.' will
            match as 'Latin', and 'あ.' will match as 'Hiragana'.  See UAX #24
            for details.

    >>> is_script('A', 'Latin')
    True
    >>> is_script('Artemísia', 'Latin')
    True
    >>> is_script('ἀψίνθιον ', 'Latin')
    False
    >>> is_script('Let θι = 3', 'Latin', ignore=['Greek', 'Common', 'Inherited', 'Unknown'])
    True
    >>> is_script('はるはあけぼの', 'Hiragana')
    True
    >>> is_script('はるは:あけぼの.', 'Hiragana')
    True
    >>> is_script('はるは:あけぼの.', 'Hiragana', ignore=[])
    False

    """

    if ignore is None:
        ignore = []

    capitalized_script = script.capitalize()
    for char in string:
        char_scripts = which_scripts(char)
        for char_script in char_scripts:
            if char_script not in ignore and char_script not in capitalized_script:
                return False
    return True

def which_scripts(char):
    """Returns: list of scripts that char belongs to.

    >>> which_scripts('z')
    ['Latin']
    >>> which_scripts('.')
    ['Common']
    >>> which_scripts('は')
    ['Hiragana']
    >>> which_scripts('،') # u+060c
    ['Arabic', 'Common', 'Hanifi_Rohingya', 'Nko', 'Syriac', 'Thaana', 'Yezidi']
    >>> which_scripts('゙') # u+3099
    ['Hiragana', 'Inherited', 'Katakana']
    >>> which_scripts("\ue000")
    ['Unknown']
    """

    cp = ord(char)
    nb_buckets = len(BUCKETS)
    steps = 65536 // nb_buckets
    index = cp // steps
    bucket = BUCKETS[index]

    # binary search within the bucket
    low, high = 0, len(bucket) - 1
    while low < high:
        mid = (low + high) // 2
        current_entry = bucket[mid][0]

        if cp <= current_entry:
            high = mid
        else:
            low = mid + 1

    return bucket[low][1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
