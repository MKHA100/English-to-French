# import translator as tr
import unittest
from . import translator as tr  

class TestCase1(unittest.TestCase):
    def test_eng_fren1(self):
        self.assertNotEqual(tr.english_to_french('Nul'), 'None')
    
    def test_eng_fren2(self):
        self.assertEqual(tr.english_to_french('Hello'), 'Bonjour')

class TestCase2(unittest.TestCase):
    def test_fren_eng1(self):
        self.assertNotEqual(tr.french_to_english('None'), 'Nul')
    
    def test_fren_eng2(self):
        self.assertEqual(tr.french_to_english('Bonjour'), 'Hello')

unittest.main()