# -*- coding: utf-8 -*-
"""
Created on Wed May 14 09:54:40 2025

@author: dalgo
"""
##TD7 Graphes

import tkinter as tk
import numpy as np
from numpy import random as rd



graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], 
[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]] #graphe fourni par l'énoncé
WIDTH = 800 #fixés arbitrairement
HEIGHT=500

# Création de la fenêtre
root = tk.Tk()
root.title("Représentation du graphe") #titre de la fenêtre

#Création d'un caneva
canvas = tk.Canvas(root, width=800, height=500, bg="white")
canvas.grid(row=1,column=1,columnspan=5, rowspan = 5)

# Création du bouton "Quitter" (non demandé par ce TD)
def quit_app():
    root.destroy()
quit_button = tk.Button(root, text="Quitter", command=quit_app)
quit_button.grid(row=6, column=2) #pady=10

#position = np.array([(rd.randint(500), rd.randint(500))
       #for i in range(len(graph))])

#exemple de dessin
def draw(canvas, graph, position):
    """
    Cette  fonction dessine un graphe 
    """
    canvas.delete('all') #pas de clear
    for i in range(len(graph)): #pour chaque sommet i et ses sucesseurs j
        for j in graph[i]:  
            canvas.create_line(position[i][0], position[i][1], position[j][0], position[j][1]) #trace une ligne entre i et j selon leurs coordonnées dans position
    for (x, y) in position:
        canvas.create_oval(x-4,y-4,x+4,y+4,fill="#f3e1d4") #trace petit cercle fermé de rayon 4 pour chaque sommet



k=1 #constante de raideur des ressorts de l'exercice

def ressort(s,t):
    """
    La force de rappel exercée par t sur s
    """
    F=[]
    l0=100
    d=np.sqrt((position[t][0]-position[s][0])**2+(position[t][1]-position[s][1])**2)
    if d == 0:
        return np.array([(0.0, 0.0)])  # Pas de force si même position
    else:
        normef=-k*(l0-d)
        fx= (position[t][0]-position[s][0])*normef/d #dx/d
        fy= (position[t][1]-position[s][1])*normef/d #dy/d
        F.append((fx,fy))
        return np.array(F)

def force(g, s):
    """
    Somme des forces pour le sommet s
    
    """
    somme = np.array([(0.0, 0.0)])
    for t in g[s]:  # uniquement les sommets adjacents
        somme += ressort(s, t)
    return somme
        
#définition de la vitesse et de la position pour chaque sommet
vit = np.array([((rd.random()-0.5)*10, (rd.random()-0.5)*10)
for i in range(len(graph))])
position = np.array([(rd.random()*500, rd.random()*500) 
for i in range(len(graph))])


def next(g, position, vit):
    """
    Cette fonction actualise les valeurs de position et de vitesse 
    de chaque sommet avec la méthode d'Euler.
    
    Garde aussi les positions de chaque sommet dans les limites
    du canva, avec 10 de marge avec les bords de la fenêtre

    """
    dt=0.01
    for i in range(len(graph)): #pour chaque sommet
        vit[i] = vit[i] + force(graph, i)[0] * dt
        position[i]=position[i]+ vit[i]*dt
        # Garde les positions dans les limites du canvas
        if position[i][0] < 10:
            position[i][0] = 10
        if position[i][0] > WIDTH - 10:
            position[i][0] = WIDTH - 10
        if position[i][1] < 10:
            position[i][1] = 10
        if position[i][1] > HEIGHT - 10:
            position[i][1] = HEIGHT - 10
    draw(canvas, graph, position)
    root.after(10, next, g, position, vit) #en rajoutant cette ligne, pas besoin de rester sur la touche f pour que l'animation continue
    

   
    
#Cliquer sur la touche f
def on_f_press(e):
    """
    Fonction pour implémenter l'appui de la touche f pour
    lancer l'animation mais non utilisée ici
    """
    if e.char=='f':
        print("La touche f a été pressée")

root.bind('<f>', lambda e : next(graph,position,vit))       
    

#Lancer l'interface graphique
draw(canvas, graph, position)
root.mainloop()