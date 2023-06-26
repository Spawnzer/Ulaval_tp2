from chercher_chaine_saisie import chercher_chaine_saisie, entrer_valeur

def chercher_chaine_fichier():  
    list = []
    with open("texte.txt") as fd:
        for line in fd:
            list.append(line)        
    res = chercher_chaine_saisie(list[0], list[1])
    print(list[0],list[1], res)

def main():
    res = 0
    ini_str,sub_str = entrer_valeur()
    with open("texte.txt", "w") as fd:
        fd.write(ini_str + "\n" + sub_str)
    chercher_chaine_fichier()
    fd.close()
if __name__ == "__main__":
    main()