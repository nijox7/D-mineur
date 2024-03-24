from random import*


## Partie cration du plateaux
def tableau(ligne, colonne):
    '''
    Creation du tableau par une liste de liste
    '''
    lstfinal =[]
    lst=[0]

    for i in range (colonne):
        lstfinal.append(lst*ligne)
    return lstfinal


def creation_mine(tableaujeux,ligne,colonne,mine):
    '''
    Place un nombre précis de mines
    à des coordonnées aléatoires sur le plateau
    puis renvoie la liste de ces dérnières
    '''
    i = 0
    listeMines=[]
    while i != mine :
        ligneMine = randint (0,ligne-1)
        colonneMine = randint (0,colonne-1)
        if (ligneMine,colonneMine) in listeMines:
           i+=0
        else:
            listeMines.append ((ligneMine,colonneMine))
            i +=1
    return listeMines


def placeMine(tableaujeux, listeMines):
    '''
    Ajoute les mines aux coordonnées indiquées dans "listecoordonne"
    '''
    for i in listeMines:
        tableaujeux [i[0]][i[1]] = "x"


def ajout_pion(i, j, tableaujeux, ligne, colonne):
    '''
    Ajoute 1 au compteur de bombes voisines de la case
    '''
    if 0 <= i < ligne and 0 <= j < colonne and tableaujeux[i][j] != "x":
        tableaujeux[i][j] += 1


def verification (i, j, tableaujeux, ligne, colonne, n=8):
    '''
    Signale la présence d'une bombe
    aux cases ---> +1 au compteur
    '''
    voisines = [0, (i-1,j+1), (i-1,j-1),
           (i+1,j+1), (i+1,j-1),
           (i,j-1), (i-1,j),
           (i,j+1), (i+1,j)]
    if n != 0:
        ajout_pion(voisines[n][0], voisines[n][1], tableaujeux, ligne, colonne)
        verification (i, j, tableaujeux, ligne, colonne, n - 1)


def numero(tableaujeux, listeMines):
    '''
    Reçoit une liste de bombes et
    les signalent à toutes leurs cases voisines
    '''
    ligne = len(tableaujeux)
    colonne = len(tableaujeux[0])
    for coord in listeMines:
        verification (coord[0], coord[1], tableaujeux, ligne, colonne)


def demine(listeCoord, decouvert):
    '''
    Découvre une case
    '''
    for coord in listeCoord:
        i, j = coord[0], coord[1]


def propage(tableaujeux, decouvert, coord):
    '''
    Propage l'explosion de la bombe
    '''
    listeDemine = []
    i, j = coord[0], coord[1]
    t_vois = [(i-1,j+1), (i-1,j-1),
           (i+1,j+1), (i+1,j-1),
           (i,j-1), (i-1,j),
           (i,j+1), (i+1,j)]
    if (0 <= i <= len(tableaujeux)-1 and 0 <= j <= len(tableaujeux[0])-1):
        case = tableaujeux[i][j]
        if case != "x" and decouvert[i][j] == 0:
            decouvert[i][j] = 1
            listeDemine.append(coord)
            if case == 0:
                for vois in t_vois:
                    listeDemine += propage(tableaujeux, decouvert, vois)
    return listeDemine