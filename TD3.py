from __future__ import annotations #donne le type avant au cas où il le reconnaît pas
import unittest  #pour pouvoir run les différents tests

##Exercice 2

#Définition de la classe Tree
class Tree:

    """

    Création d'un arbre N-aire avec comme racine "label" et comme enfants "children"
    Les étiquettes sont de type str ie chaîne de caractères

    """

    def __init__(self,label:str,*children:Tree) -> None:
        #le constructeur de la classe, initialisation d'un objet
        #avec un label et une liste d'enfants
        #*children signifie un ou plusieurs enfants
        self._label = label
        self._children = children


    def label(self)->str:
        #retourne l’étiquette du nœud (le label)
        #c'est une fonction d'accès (getter) pour self._label
        return self._label


    def children(self)-> tuple[Tree]:
        #Retourne tous les enfants du nœud, sous forme de tuple
        return self._children


    def nb_children(self)->int:
        #Retourne le nombre d’enfants que ce nœud a
        return len(self._children)


    def child(self, i:int)-> Tree :
        #Retourne le i-ème enfant de l’objet Tree
        return self._children[i]


    def is_leaf(self)->bool:
        #Vérifie si un nœud est une feuille, c'est-à-dire qu'il n'a pas d'enfants
        #Elle retourne True si le nœud est une feuille, sinon False
        if len(self._children) == 0:
            return True
        else :
            return False

##Exercice 3

    def depth(self)->int:
        #si  l'arbre n'a pas d'enfantss, c'est une feuille et la profondeur est 0
        if not self._children: #une liste contient False en booléen si elle est vide, sinon True
            return 0
        #sinon la profondeur est de 1 + la profondeur maximale des enfants de ce noeud
        else:
            return 1 + max(child.depth() for child in self._children)

##Exercice 4

    def __str__(self)->str:
        #Si l'arbre n'a pas d'enfants, il est représenté par sa valeur
        if not self._children:
            return str(self.label())
        #Sinon on construit la notation préfixée avec les enfants
        else:
            children_str = ', '.join(str(child) for child in self.children())
        return f"{self.label()}({children_str})"


#self.children est une liste contenant tous les enfants du nœud courant

#str(child) : Pour chaque enfant du nœud (chaque élément de self.children), on appelle la fonction str(child). Cela permet de convertir l'objet enfant en une chaîne de caractères. En d'autres termes, on transforme chaque enfant en sa représentation en chaîne, ce qui appelle à son tour la méthode __str__ de l'objet Tree pour les sous-arbres.

#', '.join(...) : Le résultat de la boucle est une liste de chaînes. La méthode join() permet de concaténer ces chaînes en une seule, en insérant ', ' (une virgule suivie d'un espace) entre chaque chaîne. Par exemple, si self.children contient deux nœuds qui se transforment en chaînes "b" et "c", la chaîne résultante serait "b, c".

    def __eq__(self, other) -> bool: #marche pour une prodondeur de 1
        if not isinstance(other, Tree): #vérifier que l'on compare bien deux arbres entre eux
            return False
        else:
            return self._label == other._label and self.children() == other.children()

#idée : si profondeur supérieure ou égale à 2 : vérifier à la racine, même nom , même nb enfants et profondeur et on délègue sur la suite

##Exercice 5

    def deriv(self, var : str) -> True:
# Dérivée d'une feuille (constante ou variable)
        if not self.children:
            if self.label() == var:
                return Tree('1')  #dérivée de X
            else:
                return Tree('0') #dérivée d'une cste

# Dérivée d'une addition (+)

        if self.label() == '+':
            return Tree('+', self.child(0).deriv(var), self.child(1).deriv(var))

        # Dérivée d'une multiplication (*)
        if self.label() == '*':
            f_prime = self.child(0).deriv(var)
            g_prime = self.child(1).deriv(var)
            f = self.child(0)
            g = self.child(1)
            return Tree('+', Tree('*', f_prime, g), Tree('*', f, g_prime))

        # Si l'opérateur n'est pas reconnu, on retourne l'arbre tel quel (pour d'autres opérateurs non gérés)
        return self


#Dérivée d'une constante (feuille) : La dérivée d'une constante par rapport à n'importe quelle variable est 0

#Dérivée d'une variable : La dérivée d'une variable par rapport à elle-même est 1
#Dérivée d'une addition (+) : La dérivée de f(x) + g(x) est f'(x) + g'(x)

#Dérivée d'une multiplication (*) : La dérivée de f(x) * g(x) est f'(x) * g(x) + f(x) * g'(x)

# Exemple d'utilisation
tree = Tree('+', Tree('a'), Tree('X'))
derivative = tree.deriv('X')
print(derivative)  # Devrait afficher +(0, 1)
#il doit y avoir une erreur dans ma fonction deriv mais je ne la trouve pas car le code me renvoie +(a,X) au lieu de +(0,1)

##Classe de tests

class TestTree(unittest.TestCase): #un test est à chaque fois un cas particulier

    def test_label(self):
        t1=Tree('a')
        self.assertEqual(t1.label(), t1._label)

    def test_children(self):
        t1=Tree('a')
        self.assertEqual(t1.children(), t1._children)

    def test_nb_children(self):
        t1=Tree('a')
        self.assertEqual(t1.nb_children(),len(t1._children))

    def test_is_leaf(self):
        t1=Tree('a')
        self.assertTrue(len(t1._children) == 0)


#if __name__ == "__main__": #s'éxécute que si c'est le fichier principal
    #t1=Tree('f')
    #t2=Tree('a',t1)
    #t3=Tree('b',t1)
    #unittest.main()  applique tous les tests






