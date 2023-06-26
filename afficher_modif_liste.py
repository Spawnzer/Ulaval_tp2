def imprimer_forme(list):
    for i in range(len(list[0])):
        print(*list[i])

def imprimer_fenetre(dim):
    list = [['' for i in range(dim)] for j in range(dim)]
    res = " *"
    mid = (dim-1) / 2
    for i in range(dim):
        j = i
        for j in range(dim):
            list[i][j] = res[i in (0,mid,(dim - 1)) or j in (0,mid,(dim - 1))]
    imprimer_forme(list)

def imprimer_losange(dim):
    mid = (dim-1) / 2
    res = " *"
    list = [['' for i in range(dim)] for j in range(dim)]
    for i in range(dim):
        j = 0
        for j in range(dim):
            list[i][j] += res[j in ((mid + i),(mid - i))] if i <= mid else res[j in ((i - mid),(mid + dim - 1 - i))]
    imprimer_forme(list)

def imprimer_coin(dim):
    mid = (dim-1) / 2
    res = " *"
    list = [['' for i in range(dim)] for j in range(dim)]
    for i in range(dim):
        j = 0
        for j in range(dim):
            list[i][j] = res[j < mid - i] if i <= mid else res[j >= mid + dim - i]
    imprimer_forme(list)

def imprimer_x(dim):
    list = [['' for i in range(dim)] for j in range(dim)]
    mid = (dim-1) / 2
    res = " *"
    for i in range(dim):
        j = 0
        for j in range(dim):
            list[i][j] = res[j in (i,(dim - 1 - i))] if i <= mid else res[j in (i,(mid - (i - mid)))] 
    imprimer_forme(list)

def imprimer_menu():
    print(  "Choisir une lettre identifiant le motif voulu? \n\n"
            "F : Fenetre\n"
            "L : Losange\n"
            "C : Coin\n"
            "X : Le X\n"
    )
def main():
    while True:
        choix = 'a'
        dim = ""
        while not dim.isnumeric() or int(dim) < 5 or int(dim) > 39 or not int(dim) % 2:
            dim = input("Saisir la dimension de la liste (entre 5 et 39) ")
        imprimer_menu()
        choix = input().upper()
        forme_dict = {'F': imprimer_fenetre, 'L': imprimer_losange, 'C': imprimer_coin, 'X':imprimer_x}
        while choix not in ('F','L','C','X'):
            choix = input("Entrez un choix valide\n").upper()
        forme_dict[choix](int(dim))
        while (choix not in ('O', 'N')):
            choix = input("Voulez-vous encore faire un choix de motif? O/N ").upper()
        if choix == 'N':
            break

if __name__ == "__main__":
    main()