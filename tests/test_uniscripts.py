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
from uniscripts import is_script, which_scripts

class TestUniscripts(unittest.TestCase):
    '''Unit tests for uniscripts'''

    def test_is_script(self):
        '''Test is_script method'''
        self.assertTrue(is_script('A', 'Latin'))
        self.assertTrue(is_script('Artemísia', 'Latin'))
        self.assertFalse(is_script('ἀψίνθιον ', 'Latin'))
        self.assertTrue(is_script('Let θι = 3', 'Latin',
                                  ignore=['Greek', 'Common', 'Inherited', 'Unknown']))
        self.assertTrue(is_script('はるはあけぼの', 'Hiragana'))
        self.assertTrue(is_script('はるは:あけぼの.', 'Hiragana'))
        self.assertFalse(is_script('はるは:あけぼの.', 'Hiragana', ignore=[]))

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

    def test_readme(self):
        '''Test the python samples found in the README.md file'''
        result = doctest.testfile('../README.md', optionflags=doctest.NORMALIZE_WHITESPACE)
        self.assertFalse(result.failed, "Doctests failed on README.md")

if __name__ == '__main__':
    unittest.main()
