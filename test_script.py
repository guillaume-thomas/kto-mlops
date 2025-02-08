# test_script.py

import unittest
from mon_premier_script import count_long_names

class TestNamesMethod(unittest.TestCase):
    def test_count_long_names(self):
        """Test si la fonction retourne bien le bon nombre de prénoms avec plus de 7 lettres"""
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        result = count_long_names(prenoms, 7)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
