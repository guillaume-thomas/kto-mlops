# Mon premier script corrigé

def count_long_names(prenoms, length=7):
    """
    Compte le nombre de prénoms ayant plus de 'length' lettres.
    
    Args:
        prenoms (list): Liste des prénoms.
        length (int): Seuil de longueur pour considérer un prénom comme long. Par défaut, 7.
    
    Returns:
        int: Nombre de prénoms ayant plus que 'length' lettres.
    """
    long_names_count = sum(1 for prenom in prenoms if len(prenom) > length)
    
    for prenom in prenoms:
        status = "supérieur" if len(prenom) > length else "inférieur ou égal"
        print(f"{prenom} est un prénom avec un nombre de lettres {status} à {length}.")
    
    return long_names_count


# Affichage du message initial
message = "C'est mon premier script !!!"
print(message)

# Liste des prénoms
prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]

# Exécution de la fonction et affichage du résultat
count = count_long_names(prenoms)
print(f"Nombre de prénoms dont le nombre de lettres est supérieur à 7 : {count}")  # Ligne corrigée
