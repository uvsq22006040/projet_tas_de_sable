####################################
# groupe MIASHS TD 02
# Michael GREKOBI
# Pierre-Axel RIVIERE
# Jeremy SALEH
# Ilyes MAGHLAOUA
# https://github.com/uvsq22006040/projet_tas_de_sable
####################################

########################
# import des librairies

import tkinter as tk
import random as rd


########################
# constantes

# hauteur du canvevas
HAUTEUR = 600
# largeur du canevas
LARGEUR = 600
# taille de la grille
N =3

# paramètres de l'automate:
# probabilité d'être un mur à l'initialisation:
P = 0.5

# choix des couleurs

COUL_MUR = "grey"
COUL_LIBRE = "white"


############################
# variables globales
terrain = []
grille = []




####################
# fonctions

def init_terrain():
    """Initialiser le terrain:
    * initialiser la liste carrée terrain à 2D de taille N telle
    que la case de coordonnées (i,j) vaut 1 si il y a un mur
    dessus et 0 sinon
    * initialiser la liste carrée grille à 2D de taille N
    telle que la case de coordonnées (i,j) contient l'identifiant
    du carré dessiné sur le canevas 
    * Une case est un mur avec probabilité P
    """
    global grille, terrain
    grille = []
    terrain = []
    for i in range(N):
        grille.append([0]*N)
        terrain.append([0]*N)

    for i in range(N):
        for j in range(N):
            if rd.uniform(0, 1) < P:
                terrain[i][j] = 1
                coul = COUL_MUR
            else:
                terrain[i][j] = 0
                coul = COUL_LIBRE
            largeur = LARGEUR // N
            hauteur = HAUTEUR // N
            x1 = largeur * i
            y1 = hauteur * j
            x2 = largeur * (i+1)
            y2 = hauteur * (j + 1)
            carre = canvas.create_rectangle((x1, y1), (x2, y2), fill=coul)
            grille[i][j] = carre
        
def affiche_terrain():
    """ Affiche le terrain sur le canvas"""
    for i in range(N):
        for j in range(N):
            if terrain[i][j] == 0:
                coul = COUL_LIBRE
            else:
                coul = COUL_MUR
            canvas.itemconfigure(grille[i][j], fill=coul)


def sauvegarde():
    """Ecrit la taille de la grille et les valeurs de la variable
     terrain das le fichier sauvegarde.txt
     """
    fic = open("sauvegarde.txt", "w")
    fic.write(str(N) + "\n")
    for i in range(N):
        for j in range(N):
            fic.write(str(terrain[i][j]) + "\n")
    fic.close()


def load():
    """
    Lire le fichier sauvegarde.txt et affiche dans le canvas le terrain lu
    """
    global N
    fic = open("sauvegarde.txt", "r")
    taille = fic.readline()
    N = int(taille)
    canvas.delete()
    # initialisation pour avoir des listes à la bonne taille
    init_terrain()
    print(terrain)
    i = j = 0
    for ligne in fic:
        terrain[i][j] = int(ligne)
        j += 1
        if j == N:
            j = 0
            i += 1
    print(terrain)
    affiche_terrain()
    fic.close()



#########################
# partie principale

# création des widgets
racine = tk.Tk()
racine.title("Génération de terrain")
canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR)
bouton_sauvegarde = tk.Button(racine, text="Sauvegarde", command=sauvegarde)
bouton_load = tk.Button(racine, text="Charger terrain", command=load)


# placement des widgets
canvas.grid(column=1, row=0, rowspan=10)
bouton_sauvegarde.grid(row=0)
bouton_load.grid(row=1)

init_terrain()

# boucle principale
racine.mainloop()