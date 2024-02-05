# je_change_de_type=1
# print(type(je_change_de_type))
# je_change_de_type="cousocus"
# print(type(je_change_de_type))


# 03_ligne 232 
# prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
# more_than_seven = 0 
# for prenom in prenoms:
#     if len(prenom) > 7:
#         more_than_seven += 1
#         print("Prenom supérieur à 7 : " + prenom)
#     else:
#         print("Prenom inférieur ou égal à 7 : " + prenom)
# print("Nombre de prénoms supérieurs à 7 : " + str(more_than_seven))
# specifier le type qu'on doit mettre dans la fonction like down there
# def saluer(nom: str) -> str:
#     return "Bonjour " + nom




# """
# Count names with more than seven letters
# """
# def names(prenoms):
#     more_than_seven = 0
#     for prenom in prenoms:
#         if len(prenom) > 7:
#             more_than_seven += 1
#             print("Prenom supérieur à 7 : " + prenom)
#         else:
#             print("Prenom inférieur ou égal à 7 : " + prenom)
#     return more_than_seven

# prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
# print("Nombre de prénoms supérieurs à 7 : " + str(names(prenoms=prenoms)))






# UNITTEST
# Il faut plutôt utiliser des classes(L'orienté objet : class VS dict)
# les test unitairses pour voir si le code marche avant et du coup detecter les erreurs,
#  et aussi faciliter le factoring

# import unittest

# """
# Count names with more than seven letters
# """
# def names(prenoms):
#     more_than_seven = 0
#     for prenom in prenoms:
#         if len(prenom) > 7:
#             more_than_seven += 1
#             print("Prenom supérieur à 7 : " + prenom)
#         else:
#             print("Prenom inférieur ou égal à 7 : " + prenom)
#     return more_than_seven

# class TestNamesMethod(unittest.TestCase):
#      def test_names(self):
#         prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
#         more_than_seven = names(prenoms=prenoms)
#         self.assertEqual(more_than_seven, 4)

# if __name__ == '__main__':
#     unittest.main()



# pour le devoir: ma_variable et non maVariable( )
#  if len(prenom) > 7 [Il faut plutôt la mettre dans une variable]
# outil statique d'anlyse de code,scana
# Il faut limiter les boucles à 5
# ne pas dupliquer le code, mettre dans une fonction
# Il y'a 3 trucs qui gène dans: 
#  """
# Count names with more than seven letters
# """

