def compter_prenoms(prenoms: list[str]) -> int:
    """
    Compte et affiche le nombre de prénoms dans la liste qui ont plus de 7 lettres.
    Affiche également si chaque prénom de la liste a plus de 7 lettres ou non.

    Parameters:
    prenoms (list[str]): Une liste de prénoms (chaînes de caractères).

    Returns:
    int: Le nombre de prénoms dans la liste qui ont plus de 7 lettres.
    """
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            more_than_seven += 1
            print("Prenom supérieur à 7 : " + prenom)
        else:
            print("Prenom inférieur ou égal à 7 : " + prenom)
    print("Nombre de prénoms supérieurs à 7 : " + str(more_than_seven))
    return more_than_seven

# Utilisation de la fonction
prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
nombre_prenoms_sup_7 = compter_prenoms(prenoms)


# orienté objet
def names(prenoms):
    more_than_seven = 0
    for prenom in prenoms:
        if len(prenom) > 7:
            more_than_seven += 1
            print("Prenom supérieur à 7 : " + prenom)
        else:
            print("Prenom inférieur ou égal à 7 : " + prenom)
    return more_than_seven

class TestNamesMethod(unittest.TestCase):
     def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = names(prenoms=prenoms)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()