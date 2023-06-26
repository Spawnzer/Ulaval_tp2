def chercher_chaine_saisie(ini_str, sub_str):
    res = 0
    i = 0
    while i < len(ini_str):
        if ini_str[i:i+len(sub_str)] == sub_str:
            res += 1
            i += len(sub_str)
        else:
            i += 1
    return res

def entrer_valeur():
    ini_str = input("Entrez une chaine d'au moins 4 caractères\n") 
    sub_str = input("Entrez une chaine d'au moins 1 caractères et moins que la 1ere\n") 

    while len(ini_str) < 4:
        ini_str = input("Entrez une chaine d'au moins 4 caractères\n") 
    while len(sub_str) >= len(ini_str) and len(sub_str) < 1:
        sub_str += input("Entrez une chaine d'au moins 4 caractères\n") 
    return ini_str,sub_str

def main():
    res = 0
    ini_str, sub_str = entrer_valeur()
    res = chercher_chaine_saisie(ini_str, sub_str)
    print(res)
if __name__ == "__main__":
    main()