

def count_long_names(first_names: list[str]) -> int:
    """
    Compte les prénoms qui ont plus de 7 lettres.
    Affiche pour chaque prénom s’il est long ou court.
    """
    long_name_count = 0
    for name in first_names:
        if len(name) > 7:
            long_name_count += 1
            print(f"{name} est un prénom avec un nombre de lettres supérieur à 7")
        else:
            print(f"{name} est un prénom avec un nombre de lettres inférieur ou égal à 7")
    return long_name_count




if __name__ == "__main__":
    prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
    result = count_long_names(prenoms)
    print(f"Nombre de prénoms dont le nombre de lettres est supérieur à 7 : {result}")

    print(f"Nombre de prénoms dont le nombre de lettres est supérieur à 7 : {result}")
