prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
more_than_seven = 0
for prenom in prenoms:
    if len(prenom) > 7:
        more_than_seven += 1
        print(prenom + " est un prénom avec un nombre de lettres supérieur à 7")
    else:
        print(prenom + " est un prénom avec un nombre de lettres inférieur ou égal à 7")
print("Nombre de prénoms dont le nombre de lettres est supérieur à 7 : " + str(more_than_seven))