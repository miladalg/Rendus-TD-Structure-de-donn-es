
"""
Created on Wed May 21 09:50:13 2025

@author: dalgo
"""

#Riff header : identifie le format
#fmt chunk : format audio
#data chunk : contient les echantillons audio brut
#fichier wav lu en binaire
#module struct : convertir des octets en type python
#left, right = struct.unpack('<hh', data) 
#left et right contiennent les échantillons des deux canaux 

import struct

##Exercice 1

#ouverture du fichier the wall
f = open("the_wall.wav", "rb") #r pour read le fichier et b pour ouvrir en binaire
data = f.read()
print(f"Taille totale du fichier : {len(data)} octets")
print(f"Premiers octets (en tête) : {data[0:16]}")
    
#Lecture de l'en-tête wav, c'est tout dans lexplication du format wav
nb_canaux = struct.unpack('<H', data[22:24])[0] #c'est 2, unpack renvoie un tuple avec une seule valeur
frequence = struct.unpack('<I', data[24:28])[0] #taux d'échantillonage
bits_par_echantillon = struct.unpack('<H', data[34:36])[0] #normalement 16 bits par échantillon
taille_donnees = struct.unpack('<I', data[40:44])[0] #taille de la section des données en octets
    #H pour court métrage long, I pour entier non signé ie les valeurs positives
nb_echantillons_par_voie = int(taille_donnees/(nb_canaux*bits_par_echantillon/8)) #ie par canal
    #2 octets par echantillon
    #un octet = 8 bits; un échantillon = 16 bits
    #2 canaux, donc x2 échantillons avec x2 octets
    #2 canaux car un pour oreiller gauche et un pour l'oreille droite
print(f"Canaux : {nb_canaux}")
print(f"Fréquence d'échantillonnage : {frequence} Hz")
print(f"Bits par échantillon : {bits_par_echantillon}")
print(f"Taille des données audio : {taille_donnees} octets")
print(f" Nb d'échantillons par voie : {nb_echantillons_par_voie}")
    
    #Conversion des données binaires en échantillons (numériques)
    #un échantillon = l[e volume sonore à un instant donnné
donnees_brutes = data[44: 44 + taille_donnees] #nb total d'octets,  Position de début des données audio (après 44 octets en général), donnees brute est une liste d'octets
    #'h' correspond à un entier signé h = int16
    #Le '<‘ indique que les données sont en little-endian (ordre des octets le plus courant dans les fichiers WAV).
left=[]
right=[]
    # Répartition par canal ( stéréo -> 2 voies/canaux)
for i in range(0,nb_echantillons_par_voie,2): #enumerate envoie indice puis valeur (,), ici prend un échantillon sur 2
         #à chaque instant t, echantillon left puis right [ Left_0 | Right_0 | Left_1 | Right_1 | Left_2 | Right_2 | ... ]

         #donnees brutes une liste d'octets, a un instant 4 octets
    echantillons = struct.unpack("hh", donnees_brutes[i*4:i*4+4])
         #dans echantillons, tuple avec les valeurs de left, puis right alternées
    left.append(echantillons[0])
    right.append(echantillons[1]) #mettre 0 si on prend tous les échantillons
         #hh on récupère deux fois un entier de deux octets
    
#print(left)
#print(right)
    
    
## Exercice 2

#Objectif : utiliser la liste echantillons et la transformer en son  

def write_file(left,right):
    f = open("new_wall.wav","wb") #w pour write ie si le fichier existe on l'ouvre sinon on le crée
    f.write(b"RIFF")
    f.write(struct.pack("I", 44 - 8 + len(left)*4))
    f.write(b"WAVEfmt ")
    f.write(struct.pack("IHHIIHH", 16, 1,  2, 44100, 17600, 4, 16))
    """
    16: nb de bits écrits
    1 : type de data codé
    2 : nb de canal
    44100 : taux d'échantillonage
    176400 : 44100*4, nb de bits par seconde
    4 : nb d'octets  par instant ie 2 échantillons car 2 canaux
    16 : nb de bits par échantillons
    """
    f.write(b"data")
    f.write(struct.pack("I", len(left)*4))
    for i in range(len(left)):
        f.write(struct.pack("h",left[i]))
        f.write(struct.pack("h",right[i]))
    
    
##Exercice 3

#En enlevant un échantillon sur deux, le son et la voix sont bien plus aigus

    
