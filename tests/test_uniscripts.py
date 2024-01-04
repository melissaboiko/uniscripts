'''
Unit tests for uniscripts
'''
import sys
import os
import unittest
import doctest

# Add the parent directory to the sys.path

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
# pylint: disable=import-error,wrong-import-position
from uniscripts import is_script, which_scripts, get_scripts, Scripts

class TestUniscripts(unittest.TestCase):
    '''Unit tests for uniscripts'''

    def test_is_script(self):
        '''Test is_script method'''
        self.assertTrue(is_script('A', Scripts.LATIN))
        self.assertTrue(is_script('Artemísia', Scripts.LATIN))
        self.assertFalse(is_script('ἀψίνθιον ', Scripts.LATIN))
        self.assertTrue(is_script('Let θι = 3', Scripts.LATIN,
                                  ignore=[Scripts.GREEK,
                                          Scripts.COMMON,
                                          Scripts.INHERITED,
                                          Scripts.UNKNOWN]))
        self.assertTrue(is_script('はるはあけぼの', Scripts.HIRAGANA))
        self.assertTrue(is_script('はるは:あけぼの.', Scripts.HIRAGANA))
        self.assertFalse(is_script('はるは:あけぼの.', Scripts.HIRAGANA, ignore=[]))

    def test_which_scripts(self):
        '''Test which_scripts method'''
        self.assertEqual(which_scripts('z'), ['Latin'])
        self.assertEqual(which_scripts('.'), ['Common'])
        self.assertEqual(which_scripts('は'), ['Hiragana'])
        self.assertEqual(sorted(which_scripts('،')),
                         ['Arabic', 'Common', 'Hanifi_Rohingya', 'Nko',
                          'Syriac', 'Thaana', 'Yezidi'])
        self.assertEqual(sorted(which_scripts('゙')), ['Hiragana', 'Inherited', 'Katakana'])
        self.assertEqual(which_scripts("\ue000"), ['Unknown'])

    def test_get_scripts(self):
        '''Test get_scripts method'''
        self.assertEqual(sorted(get_scripts("привет")), ['Cyrillic'])
        self.assertEqual(sorted(get_scripts("नमस्ते")), ['Devanagari'])
        self.assertEqual(sorted(get_scripts("สวัสดี")), ['Thai'])
        self.assertEqual(sorted(get_scripts("مرحبا")), ['Arabic'])
        self.assertEqual(sorted(get_scripts("გამარჯობა")), ['Georgian'])
        self.assertEqual(sorted(get_scripts("नींद")), ['Devanagari'])
        self.assertEqual(sorted(get_scripts("Γεια σας")), ['Common', 'Greek'])
        self.assertEqual(sorted(get_scripts("こんにちは")), ['Hiragana'])
        self.assertEqual(sorted(get_scripts("안녕하세요")), ['Hangul'])
        self.assertEqual(sorted(get_scripts("שלום")), ['Hebrew'])
        self.assertEqual(sorted(get_scripts("merhaba")), ['Common', 'Latin'])

    def test_get_scripts_extended_range(self):
        '''Test get_scripts in the 0x010000 to 0x110000 range'''
        self.assertEqual(sorted(get_scripts("𐲌")), ['Old_Hungarian'])
        self.assertEqual(sorted(get_scripts("𞄈𞄉𞄊𞄋")), ['Nyiakeng_Puachue_Hmong'])
        self.assertEqual(sorted(get_scripts("𑃙ନ𑃚ୱ𑃛ପ")), ['Oriya', 'Sora_Sompeng'])


    def test_readme(self):
        '''Test the python samples found in the README.md file'''
        result = doctest.testfile('../README.md', optionflags=doctest.NORMALIZE_WHITESPACE)
        self.assertFalse(result.failed, "Doctests failed on README.md")

if __name__ == '__main__':
    unittest.main()
