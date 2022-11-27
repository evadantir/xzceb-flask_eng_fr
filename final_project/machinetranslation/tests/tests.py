import unittest

from translator import english_to_french, french_to_english

def test_en_to_fr(self):
    self.assertEqual(english_to_french('Hello'),'Bonjour')

def test_fr_to_en(self):
    self.assertEqual(french_to_english('Bonjour'),'Hello')

def null_french_to_english(self):
    self.assertEqual(french_to_english(''),'')

def null_english_to_french(self):
    self.assertEqual(english_to_french(''),'')
    