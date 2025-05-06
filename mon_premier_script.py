import unittest

def names(prenoms):
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            more_than_seven += 1
    return more_than_seven

class TestNamesMethod(unittest.TestCase):
    def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        self.assertEqual(names(prenoms), 4)

if __name__ == '__main__':
    unittest.main()
