# -*- coding: utf-8 -*-
"""
Created on Wed May  7 09:48:17 2025

@author: dalgo
"""
import tkinter as tk
from numpy import random
import time
from tkinter import messagebox

max_croisements = 10
max_fils = 10

class App :
    
    def __init__(self, data): 
        """
        Création de la fenêtre
        """
        self.data = data
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=800, height=400, bg="white")
        self.canvas.grid(row= 1, column=1, columnspan = 5, rowspan = 5)
        self.root.title("Dessiner des entrelacs")
        self.colors =["blue", "red", "green", "black", "purple", "orange", "yellow", "pink", "brown", "gray", 
                  "cyan", "magenta", "lime", "teal", "violet", "indigo", "gold", "silver", "beige", "navy",
                  "maroon", "olive", "aqua", "fuchsia", "salmon", "turquoise", "chocolate", "coral", "plum", 
                  "orchid", "lavender"]
        self.positions_des_croisements = [] #stocke les positions des croisements
        self.canvas.bind("<Button-1>", self.click_sur_canva)
        self.start_time = None
        
    def redraw(self):
        self.canvas.delete("all") #Effacer le caneva
        self.draw_entrelacs(50,50,50,50)
        
    
    def read_word(self, mot, h, w, x0, y0,color):
        x,y = x0,y0 # initalisation que l'on choisit 
        for lettre in mot : # on itère sur les lettres du mot
            if lettre == "H" :
                # Trace un trait horizontal de longueur h
                self.canvas.create_line(x, y, x + h, y, fill=color,width= 3) #du point (x,y) vers le point (x+h, y), fill la couleur et width la largeur du trait
                x += h  # Mise à jour de la position
            if lettre == "U" :
                # Déplace de (w, h) vers le haut et dessine une ligne
                self.canvas.create_line(x, y, x + w, y + h, fill=color, width= 3)  #attention, les axes avec tkinter sont différents
                x += w
                y += h
            if lettre == "D":
                # Déplace de (w, -h) vers le bas et dessine une ligne
                self.canvas.create_line(x, y, x + w, y - h, fill=color, width= 3)
                x += w
                y -= h
        

    def run_forever(self): #les boutons, le label et main loop
        quit_button = tk.Button(self.root, text="Quitter", command=self.quit_app)
        quit_button.grid(row=6, column=2)
        shuffle_button = tk.Button(self.root, text="Permuter les couleurs", command=self.shuffle_colors)
        shuffle_button.grid(row=6, column=4)
        entrelacs_au_hasard_button = tk.Button(self.root, text=" Tirer au hasard un entrelac", command=self.entrelacs_au_hasard)
        entrelacs_au_hasard_button.grid(row=7, column=2)
        self.root.mainloop()
   
        
    def draw_entrelacs(self, h, w, x0, y0):
        """
        Fonction qui dessine les entrelacs
        """
        self.positions_des_croisements = [] #réinitialisation des clicks
        indicecouleur=0
        for mot in self.data.tableau_vers_mots():#on crée une ligne brisée pour chaque mot, 4 mots
            color=self.colors[indicecouleur]
            self.read_word(mot, h, w, x0, y0, color) #a pour argument la couleur (exercice 3)
            indicecouleur+=1
            y0 += h  #Décalage pour chaque ligne suivante 
            
        for index, fil in enumerate(self.data.tableau): #dessiner des petits cercles pour cliquer sur les croisements
            x = x0 + 2*index*w
            y= 50 + fil*h
            self.positions_des_croisements.append((x,y,index)) #stocker pour le clic
            self.canvas.create_oval(x-4, y-4, x+4, y+4, outline='black') #repère visuel
            
    def quit_app(self):
        self.root.destroy()

    def shuffle_colors(self):
        random.shuffle(self.colors)
        self.redraw()
        
    def entrelacs_au_hasard(self):
        self.data.n = random.randint(2,max_fils)
        self.data.tableau = [random.randint(0,self.data.n-2) for _ in range(random.randint(1,max_croisements))]
        self.redraw()
       
    def click_sur_canva(self,event):
        eps=10
        for x,y, index in self.positions_des_croisements:
            if abs(event.x -x)< eps and abs(event.y - y)<eps:
                self.appliquer_reidemeister(index)
                break
    
    def appliquer_reidemeister(self, index):
        if index >= len(self.data.tableau):
            return
        c1 = self.data.tableau[index]
        # Chercher un second croisement identique sans croisement entre les deux qui touche les mêmes fils
        for j in range(index + 1, len(self.data.tableau)):
            if self.data.tableau[j] == c1:
            # Vérifie qu'aucun croisement entre index+1 et j ne touche les mêmes fils (c1 ou c1+1)
                if all(abs(self.data.tableau[k] - c1) > 1 for k in range(index + 1, j)):
                # Supprimer les deux croisements (on supprime d'abord le second pour éviter les problèmes d'index)
                    del self.data.tableau[j]  # Supprimer le deuxième croisement
                    del self.data.tableau[index]  # Supprimer le premier croisement
                
                    self.redraw()  # Redessiner la structure

                    # Remise à l'index précédent pour vérifier s'il y a d'autres croisements à supprimer
                    self.appliquer_reidemeister(index)
                    # Vérifie la fin de partie
                    self.verifier_fin()
                    return  # Quitter après avoir appliqué le mouvement

    def nouvelle_partie(self):
        self.start_time = time.time()
        
    def verifier_fin(self):
    # Si tous les croisements ont été supprimés
        if not self.data.tableau:
            elapsed = time.time() - self.start_time
        # Affiche une petite fenêtre avec le temps de jeu
            messagebox.showinfo(
                "Bravo !",
                f"Vous avez dénoué tous les nœuds en {elapsed:.2f} secondes !"
            )
    # sinon, on ne fait rien : pas de félicitations tant qu'il reste des coups possibles

    
class Data :
    
    def __init__(self,tableau, n): #n nb de fils, tableau la définition de l'entrelacement
        self.tableau = tableau
        self.n=n
        
    def tableau_vers_mots(self): #n le nb de fils, le tableau c'est la liste de valeurs
        mots = []
        for i in range(self.n): #pour chaque fil i
            mot = "H"
            f=i
            for j in range(len(self.tableau)): #pour chaque valeur dans le tableau
                if self.tableau[j] == f :
                    mot+="U" #U c'est qu'on descend
                    f+=1
                elif self.tableau[j] == f-1 :
                    mot+="D"
                    f-=1
                else :
                    mot+="H"
                mot+="H"
            mots.append(mot)
        return mots 
        

#mouvement de Reidemeister = deux fils s’entrelacent puis se dénouent  



if __name__ == "__main__": #éxécute le fichier principal
    data = Data([],2)
    app = App(data)
    app.run_forever()