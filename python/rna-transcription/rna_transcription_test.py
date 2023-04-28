"""RNA Transcription Test Module"""
import unittest

from rna_transcription import to_rna

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.3.0


class RnaTranscriptionTest(unittest.TestCase):
    """RNA Transcription Test class"""
    def test_empty_rna_sequence(self):
        """Test with an empty string"""
        self.assertEqual(to_rna(""), "")

    def test_transcribes_cytosine_to_guanine(self):
        """Test for translation of C to G"""
        self.assertEqual(to_rna('C'), 'G')

    def test_transcribes_guanine_to_cytosine(self):
        """Test for translation of G to C"""
        self.assertEqual(to_rna('G'), 'C')

    def test_transcribes_thymine_to_adenine(self):
        """Test for translation of T to A"""
        self.assertEqual(to_rna('T'), 'A')

    def test_transcribes_adenine_to_uracil(self):
        """Test for translation of A to U"""
        self.assertEqual(to_rna('A'), 'U')

    def test_transcribes_all_occurrences(self):
        """Test for translation of string to complement"""
        self.assertEqual(to_rna('ACGTGGTCTTAA'), 'UGCACCAGAAUU')


if __name__ == '__main__':
    unittest.main()
