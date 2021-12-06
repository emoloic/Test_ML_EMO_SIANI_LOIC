#!/usr/bin/python

# Importation des libraries et fonctions nécessaires
import os
import sys
from time import sleep
from fonctionsTri import *
from threading import Thread



# Fonction tri_buche
def tri_buche(nom_fichier):
    """
        Cette fonction prend en argument le nom d'un fichier texte qui contient une suite de nombres entre 0 et 500 tous séparé par un espace (sur une seule ligne) et
        effectue le tri dichotomique et le tri Shaker des nombres contenus dans le fichier et renvoi les valeurs triées par les deux méthodes dans la console.
    """
    if os.path.exists(nom_fichier):
        with open(nom_fichier,"r+") as file:
            # Récupération des différentes valeurs (longueur des buches) contenu dans notre fichier
            longueur_buches = file.read().split(' ')
            # Conversion en une liste d'éléments entiers.
            longueur_buches = [int(i) for i in longueur_buches]
            # Création des threads
            thread1 = Thread(target=tri_dichotomique, name="Thread 1", args=(longueur_buches,))
            thread2 = Thread(target=tri_shaker, name="Thread 2", args=(longueur_buches,))
            # Démarrage des threads
            thread1.start()
            thread2.start()
            # Attente de la fin d'exécution de tout nos threads
            thread1.join()
            thread2.join()
            # Fermeture de notre fichier
            file.close()
    else:
        print("Désolé, le nom de fichier spécifié n'existe pas.")

if __name__ == "__main__":
    tri_buche(sys.argv[1])