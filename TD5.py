# -*- coding: utf-8 -*-
"""
Created on Wed Apr 30 09:50:28 2025

@author: dalgo
"""
##td5 

import tkinter as tk
from numpy import random #utile pour l'utilisation de random




## Exercice 1

 
def read_word(canvas, mot, h, w, x0, y0,color):
    x,y = x0,y0 # initalisation que l'on choisit 
    for lettre in mot : # on itère sur les lettres du mot
        if lettre == "H" :
            # Trace un trait horizontal de longueur h
            canvas.create_line(x, y, x + h, y, fill=color,width= 3) #du point (x,y) vers le point (x+h, y), fill la couleur et width la largeur du trait
            x += h  # Mise à jour de la position
        if lettre == "U" :
            # Déplace de (w, h) vers le haut et dessine une ligne
            canvas.create_line(x, y, x + w, y + h, fill=color, width= 3)  #attention, les axes avec tkinter sont différents
            x += w
            y += h
        if lettre == "D":
            # Déplace de (w, -h) vers le bas et dessine une ligne
            canvas.create_line(x, y, x + w, y - h, fill=color, width= 3)
            x += w
            y -= h
    
# Explication de la commande create_lines

# canvas.create_line(50, 50, 200, 50, fill="blue", width=3)
# Ce code trace une ligne bleue de 3 pixels d'épaisseur partant du point (50, 50) et se terminant au point (200, 50). La ligne sera horizontale.

# Création de la fenêtre
root = tk.Tk()
root.title("Interpréteur de mots dessinables") #titre de la fenêtre
    
# Création d'un canvas
canvas = tk.Canvas(root, width=800, height=400, bg="white")
canvas.pack()
    
# Mot à dessiner, h et w
#mot = "HUHHDUH"
##h = 50  # Hauteur des déplacements
w = 50  # Largeur des déplacements
    
# Appel de la fonction pour dessiner le mot
#read_word(canvas,"HUHHDUH", h, w)
    
  
    
  
    
  
    
  
##Exercice 2 et 3
    
root.title("Dessiner des entrelacs")    #titre de la fenêtre
    
def tableau_vers_mots(tableau,n): #n le nb de fils, le tableau c'est la liste de valeurs
    mots = []
    for i in range(n): #pour chaque fil i
        mot = "H"
        f=i
        for j in range(len(tableau)): #pour chaque valeur dans le tableau
            if tableau[j] == f :
                mot+="U" #U c'est qu'on descend
                f+=1
            elif tableau[j] == f-1 :
                mot+="D"
                f-=1
            else :
                mot+="H"
            mot+="H"
        mots.append(mot)
    return mots              



#Fonction pour dessiner des entrelacs

def draw_entrelacs(canvas, h, w, x0, y0):
    """
    Fonction qui dessine les entrelacs
    """
    indicecouleur=0
    for mot in tableau_vers_mots(valeurs,4):#on crée une ligne brisée pour chaque mot, 4 mots
        color=Couleurs[indicecouleur]
        read_word(canvas, mot, h, w, x0, y0,color) #a pour argument la couleur (exercice 3)
        indicecouleur+=1
        y0 += h  #Décalage pour chaque ligne suivante 
    
Couleurs = ["blue", "red", "green", "black", "purple", "orange"]
valeurs= [2, 1, 1, 0, 2]
# et 4 fils
draw_entrelacs(canvas, 50,50, 50,50)










## Exercice 4

# Fonction pour quitter l'application
def quit_app():
    root.destroy()

# Fonction pour permuter les couleurs
def shuffle_colors():
    random.shuffle(Couleurs)
    canvas.delete("all")  # Effacer le canevas
    draw_entrelacs(canvas, 50, 50, 50, 50)  # Redessiner avec les couleurs permutées

# Création du bouton "Quit"

quit_button = tk.Button(root, text="Quitter", command=quit_app)
quit_button.pack(side=tk.BOTTOM, padx=10, pady=10)

# Création du bouton "Permuter les couleurs"
shuffle_button = tk.Button(root, text="Permuter les couleurs", command=shuffle_colors)
shuffle_button.pack(side=tk.BOTTOM, padx=10, pady=10) #pack() permet d'ajouter un widget








## Exercice 5

#def afficher_tableau_croisements(valeurs):
    #tableau_str = "Croisements :         ["
    #for index, valeur in enumerate(valeurs):
        #tableau_str += f"{valeur},"
    #tableau_str+="]"
    #return tableau_str

#Affichage du tableau de croisement sur la fenêtre

#tableau_croisements = afficher_tableau_croisements(valeurs)
tableau_label = tk.Label(root, text=f"Croisements : {valeurs}", anchor="w", justify="left")
tableau_label.pack(side=tk.TOP, padx=10, pady=10)


#Lancer l'interface graphique
root.mainloop()






## Exercice 6
#je n'ai pas réussi cet exo, mais voici une proposition


# Marges
marge_x = 20
marge_y = 20

canvas_width = int(canvas["width"]) #Largeur
canvas_height = int(canvas["height"]) #Hauteur

# Calcul dynamique de w et h
#w = (canvas_width - 2 * marge_x) // (nb_croisements * 2)  # *2 car il y a 2 lettres H/U ou H/D par croisement
#h = (canvas_height - 2 * marge_y) // (nb_fils + 1)         # +1 pour espacer

# Point de départ
x0 = marge_x
y0 = marge_y

draw_entrelacs(canvas, (canvas_height - 2 * marge_y) // (nb_fils + 1) ,(canvas_width - 2 * marge_x) // (nb_croisements * 2), 50,50)






    
    