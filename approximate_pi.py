#! /usr/bin/env python3

"""module chargé de calculer une approximation de pi"""

import sys
import random

def approxim_pi(nb_points):
    """génère n points aléatoiresdans [-1,1]² et vérifie
    si ce point est dans le cercle de rayon 1 centré en 0"""
    liste,compteur,liste_approx_pi  = [],0,[]
    for k in range(nb_points):
        absx,ordy = random.uniform(-1,1),random.uniform(-1,1)
        res = ((absx)**2 + (ordy)**2)**(1/2) <= 1
        liste += [[absx,ordy, res]]
        compteur += res*1
        if k % (nb_points//10) == 0 and k != 0:
            liste_approx_pi += [(compteur*4)/k]
    if len(liste_approx_pi) != 10:
        liste_approx_pi += [(compteur*4)/nb_points]
    return liste,liste_approx_pi

def main():
    """génère n points aléatoiresdans [-1,1]² et vérifie
    si ce point est dans le cercle de rayon 1 centré en 0"""
    entree = sys.argv
    if len(entree) != 2:
        raise IndexError("./approximate.py nb_points")
    nb_points = int(entree[1])
    compteur  = 0
    for _ in range(nb_points):
        absx,ordy = random.uniform(0,1),random.uniform(0,1)
        res = ((absx)**2 + (ordy)**2)**(1/2) <= 1
        compteur += res*1
    approx_pi = (compteur*4)/nb_points
    print(approx_pi)

if __name__ == "__main__":
    main()