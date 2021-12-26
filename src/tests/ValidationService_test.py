
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from services import validation_service

CORRECT_FILENAME = os.path.join(os.path.dirname(__file__), 'testfiles/histodata.txt')
WRONG_FILENAME = os.path.join(os.path.dirname(__file__), 'testfiles/histogram.png')

class TestValidationService(unittest.TestCase):

    def test_file_type(self):
        val = ValidationService.file_type(CORRECT_FILENAME)
        self.assertEqual(val, True)

    def test_file_type_fails(self):
        val = ValidationService.file_type(WRONG_FILENAME)
        self.assertEqual(val, False)

    def test_is_fasta(self):
        val = ValidationService.is_fasta(CORRECT_FILENAME)
        self.assertEqual(val, True)
