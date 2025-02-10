import unittest

def count_long_names(names_list, length_threshold=7):
    """
    Count the amount of names with size higher than the specified threshold and
    prints a message indicating if it's higher or lower than this number.
    The threshold is 7 by default.
    """
    long_names = [name for name in names_list if len(name) > length_threshold]
    
    for name in names_list:
        comparison = "supérieur" if len(name) > length_threshold else "inférieur ou égal"
        print(f"{name} est un prénom avec un nombre de lettres {comparison} à {length_threshold}")
    
    return len(long_names)

class TestCountLongNames(unittest.TestCase):
    def test_count_long_names(self):
        first_names = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        result = count_long_names(first_names)
        self.assertEqual(result, 4)

if __name__ == '__main__':
    first_names = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
    count = count_long_names(first_names)
    print(f"Nombre de prénoms dont le nombre de lettres est supérieur à 7 : {count}")
    unittest.main()
