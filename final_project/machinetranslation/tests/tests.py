import unittest
from translator import english_to_french, french_to_english

class TestTranslation(unittest.TestCase): 
    def testEnglishToFrench(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french(''), '')
        
    def testFrenchToEnglish(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english(''), '')
        
unittest.main()