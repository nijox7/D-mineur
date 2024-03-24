from fltk import*

## Partie graphique.


def plateau(tableaujeux, ligne, colonne, mine):
    x = 900
    y= 900
    cree_fenetre(x, y)
    menu(ligne, colonne, x, y, mine)
    liste = carre(tableaujeux, x, y, ligne, colonne, mine)
    return liste


def menu(ligne, colonne, x, y, mine):
    rectangle(0, 0, x, (y/ligne))
    texte ((x/(colonne)), (y/(ligne))/2, "Au milieu", taille=10, ancrage="center")
    texte (((x/(colonne)))*3, (y/(ligne))/2,"Bombe restante", taille=10, ancrage ="center")
    texte (((x/(colonne)))*5, (y/(ligne))/2, "Timer", taille=10, ancrage="center")


def carre(tableaujeux, x, y, ligne, colonne, mine):
    lst = [] * len(tableaujeux)
    n=0
    for i in range(ligne):
        lst.append([])
        for j in range(colonne):
            if n%2 == 0:
                couleur = "dark green"
            else:
                couleur = "green"
            texte ((x/(colonne)) * j, (y/(ligne+1)) * (i+1), str(tableaujeux[i][j]))
            rectangle ((x/(colonne)) * j, (y/(ligne+1)) * (i+1),
                       (x/(colonne)*j) + x/(colonne), (y/(ligne+1)) * (i+1) + (y/(ligne+1)),
                        tag="case"+str(i)+str(j))
            rectangle ((x/(colonne)) * j, (y/(ligne+1)) * (i+1),
                       (x/(colonne)*j) + x/(colonne), (y/(ligne+1)) * (i+1) + (y/(ligne+1)),
                        remplissage=couleur, tag="case"+str(i)+str(j))
            lst[i].append ([(x/(colonne)) * j, (y/(ligne+1)) * (i+1),
                         (x/(colonne)*j) + x/(colonne), (y/(ligne+1)) * (i+1) + (y/(ligne+1))])
            n += 1
        n += 1
    return lst


def donne_case(listeCoord, tableaujeux, ev):
    x = abscisse(ev)
    y = ordonnee(ev)
    for ligne in range (len(listeCoord)):
        for col in range (len(listeCoord[0])):
            coord = listeCoord[ligne][col]
            if coord[0] < x < coord[2] and coord[1] < y < coord[3]:
                return (ligne, col)
    return None


def action_clic_droit (i,x,y,coord):
    rectangle (i[0],i[1],i[2],i[3],remplissage = 'red')
    coord.remove (i)


def marqueCase(listeCoord, ligne, col, couleur):
    coord = listeCoord[ligne][col]
    ax, ay = coord[0], coord[1]
    bx, by = coord[2], coord[3]
    rectangle(ax, ay, bx, by, tag=couleur+str(ligne)+str(col), remplissage=couleur)


def detruitCase(decouvert, listeCoord):
    for ligne in range(len(decouvert)):
        for col in range(len(decouvert[0])):
            if decouvert[ligne][col] == 1:
                efface("case"+str(ligne)+str(col))