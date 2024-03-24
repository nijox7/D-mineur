from modele import *
from vue import*

## Creation du jeux

#Paramètres
ligne = 12
colonne = 12
mine = 20
tableaujeux = tableau (ligne, colonne)
decouvert = []
for i in range(ligne):
    decouvert.append([])
    for j in range(colonne):
        decouvert[i].append(0)
listeMines = creation_mine(tableaujeux, ligne, colonne, mine)
placeMine(tableaujeux,listeMines)
n=8
numero(tableaujeux, listeMines)
for i in tableaujeux:
    print (i)
#Créer le plateau et enregistre la positon des cases
listeCoord = plateau(tableaujeux, ligne, colonne, mine)

while True:
    ev = attend_ev()
    tev = type_ev(ev)
    if tev == "Quitte":
        break

    elif tev == "ClicDroit":
        print("Clic droit au point", (abscisse(ev), ordonnee(ev)))
        coord = donne_case(listeCoord, tableaujeux, ev)
        if coord != None:
            ligne, col = coord[0], coord[1]
            if decouvert[ligne][col] == 2:
                efface("red"+str(ligne)+str(col))
                decouvert[ligne][col] = 0
            else:
                marqueCase(listeCoord, ligne, col, "red")
                decouvert[ligne][col] = 2

    elif tev == "ClicGauche":
        print("Clic gauche au point", (abscisse(ev), ordonnee(ev)))
        coord = donne_case(listeCoord, tableaujeux, ev)
        if coord != None:
            ligne, col = coord[0], coord[1]
            case = tableaujeux[ligne][col]
            print(case)
            if case == 'x':
                efface("case"+str(ligne)+str(col))
                texte(300, 300, "PERDU", couleur="red", taille=40)
                attend_ev()
                break
            elif decouvert[ligne][col] == 0:
                listeDemine = propage(tableaujeux, decouvert, coord)
                demine(listeDemine, decouvert)
                detruitCase(decouvert, listeCoord)

    mise_a_jour()
ferme_fenetre()
