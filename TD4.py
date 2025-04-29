## TD4 Hachage

import matplotlib.pyplot as plt

#Exercice 2

def naive_fonction(key):
    return sum(ord(c) for c in key)


class Hashtable:

    """

    définition de la classe "table de hachage"


    """

    def __init__(self,h=naive_fonction, N:int=10): #N est la taille de la table, h la fonction de hachage
        self.N=N
        self.table= [[] for _ in range (N)] #création de liste de listes vide, underscore comme une variable
        self._h = h

    def put(self,key,value):
        index = self._h(key) % self.N #l'index c'est le numéro de la case
        for j in range(len(self.table[index])): #j l'indice du couple dans la sous-liste qui correspond à l'index
            if key == self.table[index][j][0]: #on regarde dans la sous-liste qui correspond à l'index, pour chaque tuple j, dans les clés [O], si il y a key
                self.table[index][j]=(key,value) #un couple est non mutable donc on remplace par couple pas par clé ou valeur
                return
        self.table[index].append((key,value)) #on fait ça si on rentre pas dans le if

#Exercice 3
    def get(self,value):
        index = self._h(key) % self.N
        for j in range(len(self.table[index])):
            if key == self.table[index][j][0]:
                return(self.table[index][j][1])
        return None

#Exercice 4
    def repartition(self):
        y=[]
        for i in range(len(self.table)):
            y.append(len(self.table[i])) #y est la liste des tailles de chaque sous-liste de la table
        x = range(len(y)) #x est l'index, donc l'indice de chaque sous-liste
        width = 1/1.5
        plt.bar(x, y, width, color="blue")
        plt.show()


#nouvelle fonction de hachage donnée par le prof
 
    def hash_fonction(self):
        h = 0
        off = 0
        self.count =len(self.value)-off
        for i in range(self.count):
            h = 31 * h + ord(self.value[off])
            off += 1
        return h 

#Exercice 6     
    def resize(self):
        """Double la capacité de la table et réinsère les éléments""" 
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0  # Remis à jour lors du ré-insertion

        for entry in old_table:
            if entry is not None:
                key, value = entry
                self.put(key, value)
    
    
#Exécution de l'exercice 5
f = open("frenchssaccent.txt",'r') #ouverture du fichier enregistré au même endroit que ce fichier là
L1=Hashtable(naive_fonction,320)
for mot in f.readlines(): #on lit  chaque ligne de f
    L1.put(mot.strip(), len(mot.strip()))
L1.repartition()


#exécution de l'exercice 3
L=Hashtable(naive_fonction,10) #mon objet
L.put('abc',3)
L.repartition()
print(L.table)
#L=('abc',3)
#print(naive_fonction(L))

