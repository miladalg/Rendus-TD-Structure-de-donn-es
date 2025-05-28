#créer algo pour trouver le mot de longueur maximale

tirage = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
 "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","?"] 
#tirage de toutes les lettres de l'alphabet

valeurs_lettres = {
    **dict.fromkeys(['A','E','I','L','N','O','R','S','T','U'], 1),
    **dict.fromkeys(['D','G','M'], 2),
    **dict.fromkeys(['B','C','P'], 3),
    **dict.fromkeys(['F','H','V'], 4),
    **dict.fromkeys(['J','Q'], 8),
    **dict.fromkeys(['K','W','X','Y','Z'], 10)
}
#on associe à chaque lettre un score

#ouverture du fichier, enregistré au même endroit que ce code pythons ie dans le même dossier
f = open("mots.sansaccent.txt",'r')
lexique=[]
for ligne in f:
    lexique.append(ligne[0:len(ligne)-1])
#print(lexique)


def ecrire_mot(mot,tirage): 
    """On définit une fonction qui vérifie 
    si on peut écrire un mot donné 
    avec un tirage donné
    """
    copie_tirage = tirage.copy() #On réalise une copie de tirage car une lettre de cette liste ne peut être utilisée qu'une seule fois donc il faut la retirer de la copie de tirage une fois examinée
    mot_possible = True
    joker_utilise = False
    for lettre in mot:
        if lettre in copie_tirage:
            copie_tirage.remove(lettre)
        elif '?' in copie_tirage and not joker_utilise:
            copie_tirage.remove('?')
            joker_utilise = True
        else:
            mot_possible = False
            break
    return mot_possible

def liste_mots(lexique,tirage): 
    """On définit une fonction donnant la liste 
    des mots que l'on peut écrire avec
    un tirage donné 
    """
    mots_possibles = []
    for mot in lexique:
        if ecrire_mot(mot,tirage): #ie si ça renvoie True
            mots_possibles.append(mot)
    return mots_possibles

#par ex : ecrire_mot("chat", ['c','h','a','t','e']) -> renvoie True ie on peut écrire le mot chat avec le tirage donné

def plus_long_mot(lexique, tirage):
    mots_possibles = liste_mots(lexique, tirage)
    if not mots_possibles:
        return ""
    return max(mots_possibles, key=len)



def score(mot):
    """
    calcule le score d'un mot
    """
    return sum(valeurs_lettres.get(l.upper(), 0) for l in mot)


def max_score(tirage, lexique):
    """
    Cherche le plus long mot de lexique pouvant être formé avec les lettres de tirage
    (et un joker) et qui rapporte le maximum de points
    """
    # initialisation de la solution
    meilleur_mot = ""
    meilleur_score = 0

    for mot in lexique:
        lettres_dispo = list(tirage) #ou tirage.copy()
        est_valide = True
        lettres_joker = [] #Lettres remplacées par '?'
        joker_utilise = False

        # Vérifie que le mot peut être formé avec le tirage
        for lettre in mot:
            if lettre in lettres_dispo:
                lettres_dispo.remove(lettre)
            elif '?' in lettres_dispo and not joker_utilise:
                lettres_dispo.remove('?')
                lettres_joker.append(lettre)
                joker_utilise = True
            else:
                est_valide = False
                break

        # Si le mot est valide, calcule son score
        if est_valide:
            score_mot = 0
            for lettre in mot:
                if lettre in lettres_joker:
                    lettres_joker.remove(lettre)
                else :
                    score_mot += valeurs_lettres.get(lettre.upper(), 0)
                    #lettre.upper() transforme la lettre minuscule en lettre majuscule
                    # .get(...,0) cherche la valeur associée dans le dico, 
                    # si valeur non trouvée, retourne 0
            if score_mot > meilleur_score:
                meilleur_score = score_mot
                meilleur_mot = mot
        #print(lettres_joker)
    return meilleur_mot, meilleur_score

print(max_score(tirage, lexique))
print(score("xylographiques"))





