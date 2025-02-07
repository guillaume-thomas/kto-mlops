import unittest

"""
Count names with more than seven letters
"""
def compte_les_mots_depassant_strictement_le_nombre_de_lettre_vise(liste_prenoms: list , nombre_lettre: int) -> int:
    compteur_mots = 0
    for prenom in liste_prenoms:
        if len(prenom) > nombre_lettre:
            compteur_mots += 1
    return compteur_mots

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        liste_prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        nombre_lettre = 7
        more_than_seven = compte_les_mots_depassant_strictement_le_nombre_de_lettre_vise(liste_prenoms=liste_prenoms, nombre_lettre=nombre_lettre)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()