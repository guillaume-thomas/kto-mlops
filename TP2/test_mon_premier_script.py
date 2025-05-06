import unittest
from mon_premier_scriptfinal import count_long_names



class TestCountLongNames(unittest.TestCase):
    def test_count_long_names(self):
        names = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        expected = 4  # Guillaume, Juliette, François, Cassandre
        self.assertEqual(count_long_names(names), expected)


if __name__ == "__main__":
    unittest.main()
