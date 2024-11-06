#! /usr/bin/env python3

"""génération d'images PPM puis d'un GIF"""

import sys
import subprocess
import copy
import approximate_pi

def segment(depart,arrivee,matrix,epaisseur):
    """si le segment est horizontale, le départ est à gauche
    De même si le segment est verticale, le départ doit être en haut"""
    if depart[0] == arrivee[0]:
        for i in range(epaisseur+1):
            for k in range(depart[1],arrivee[1]+1):
                matrix[k][depart[0]+i] = "0 0 0 \n"
    else:
        for i in range(epaisseur+1):
            for k in range(depart[0],arrivee[0]+1):
                matrix[depart[1]+i][k] = "0 0 0 \n"

def point(matrix,pointeur,epaisseur):
    """écrit un point dans la matrice"""
    for i in range(epaisseur+1):
        for j in range(epaisseur+1):
            matrix[pointeur[1]+i][pointeur[0]+j] = "0 0 0 \n"
    pointeur = (pointeur[0]+ epaisseur*2,pointeur[1])
    return pointeur

def write_digit(number,matrix,pointeur,epaisseur,hauteur_digit,largeur_digit):
    """Ecris un chiffre sur l'image ppm"""
    if number == 1:
        debut = (pointeur[0],pointeur[1] + epaisseur)
        arrivee = (pointeur[0],pointeur[1]-hauteur_digit)
        segment(arrivee,debut,matrix,epaisseur)
        pointeur = (arrivee[0] + epaisseur* 2,pointeur[1])
        return pointeur
    elif number == 2:
        debut1 = pointeur
        arrivee1 = (debut1[0] + largeur_digit,debut1[1])
        debut2 =( pointeur[0],pointeur[1]-hauteur_digit//2)
        arrivee2 = (arrivee1[0],debut2[1] + epaisseur)
        debut3 = (pointeur[0],pointeur[1]-hauteur_digit)
        arrivee3 = (arrivee1[0],debut3[1])
        segment(debut1,arrivee1,matrix,epaisseur)
        segment(debut2,arrivee2,matrix,epaisseur)
        segment(debut3,arrivee3,matrix,epaisseur)
        segment(debut2,debut1,matrix,epaisseur)
        segment(arrivee3,arrivee2,matrix,epaisseur)
        pointeur = arrivee1[0] + epaisseur*2,arrivee1[1]
        return pointeur
    elif number == 3:
        debut1 = pointeur
        arrivee1 = (debut1[0] + largeur_digit,debut1[1] + epaisseur)
        debut2 =( pointeur[0],pointeur[1]-hauteur_digit//2)
        arrivee2 = (arrivee1[0],debut2[1])
        debut3 = (pointeur[0],pointeur[1]-hauteur_digit)
        arrivee3 = (arrivee1[0],debut3[1])
        segment(debut1,arrivee1,matrix,epaisseur)
        segment(debut2,arrivee2,matrix,epaisseur)
        segment(debut3,arrivee3,matrix,epaisseur)
        segment(arrivee2,arrivee1,matrix,epaisseur)
        segment(arrivee3,arrivee2,matrix,epaisseur)
        pointeur = arrivee1[0] + epaisseur*2,arrivee1[1] - epaisseur
        return pointeur
    elif number == 4:
        debut1 = pointeur
        arrivee1 = (debut1[0] + largeur_digit,debut1[1] + epaisseur)
        debut2 =( pointeur[0],pointeur[1]-hauteur_digit//2)
        arrivee2 = (arrivee1[0],debut2[1])
        debut3 = (pointeur[0],pointeur[1]-hauteur_digit)
        arrivee3 = (arrivee1[0],debut3[1])
        segment(debut2,arrivee2,matrix,epaisseur)
        segment(arrivee2,arrivee1,matrix,epaisseur)
        segment(arrivee3,arrivee2,matrix,epaisseur)
        segment(debut3,debut2,matrix,epaisseur)
        pointeur = arrivee1[0] + epaisseur*2,arrivee1[1]-epaisseur
        return pointeur
    elif number == 5:
        debut1 = pointeur
        arrivee1 = (debut1[0] + largeur_digit,debut1[1] + epaisseur)
        debut2 =( pointeur[0],pointeur[1]-hauteur_digit//2)
        arrivee2 = (arrivee1[0],debut2[1])
        debut3 = (pointeur[0],pointeur[1]-hauteur_digit)
        arrivee3 = (arrivee1[0] + epaisseur,debut3[1])
        segment(debut1,arrivee1,matrix,epaisseur)
        segment(debut2,arrivee2,matrix,epaisseur)
        segment(debut3,arrivee3,matrix,epaisseur)
        segment(arrivee2,arrivee1,matrix,epaisseur)
        segment(debut3,debut2,matrix,epaisseur)
        pointeur = arrivee1[0] + epaisseur*2,arrivee1[1] - epaisseur
        return pointeur
    elif number == 6:
        debut1 = pointeur
        arrivee1 = (debut1[0] + largeur_digit,debut1[1] + epaisseur)
        debut2 =( pointeur[0],pointeur[1]-hauteur_digit//2)
        arrivee2 = (arrivee1[0],debut2[1])
        debut3 = (pointeur[0],pointeur[1]-hauteur_digit)
        arrivee3 = (arrivee1[0] + epaisseur,debut3[1])
        segment(debut1,arrivee1,matrix,epaisseur)
        segment(debut2,arrivee2,matrix,epaisseur)
        segment(debut3,arrivee3,matrix,epaisseur)
        segment(arrivee2,arrivee1,matrix,epaisseur)
        segment(debut3,debut2,matrix,epaisseur)
        segment(debut2,debut1,matrix,epaisseur)
        pointeur = arrivee1[0] + epaisseur*2,arrivee1[1]-epaisseur
        return pointeur
    elif number == 7:
        debut1 = pointeur
        arrivee1 = (debut1[0] + largeur_digit,debut1[1] + epaisseur)
        debut2 =( pointeur[0],pointeur[1]-hauteur_digit//2)
        arrivee2 = (arrivee1[0],debut2[1])
        debut3 = (pointeur[0],pointeur[1]-hauteur_digit)
        arrivee3 = (arrivee1[0],debut3[1])
        segment(debut3,arrivee3,matrix,epaisseur)
        segment(arrivee2,arrivee1,matrix,epaisseur)
        segment(arrivee3,arrivee2,matrix,epaisseur)
        pointeur = arrivee1[0] + epaisseur*2,arrivee1[1]-epaisseur
        return pointeur
    elif number == 8:
        debut1 = pointeur
        arrivee1 = (debut1[0] + largeur_digit,debut1[1] + epaisseur)
        debut2 =( pointeur[0],pointeur[1]-hauteur_digit//2)
        arrivee2 = (arrivee1[0],debut2[1])
        debut3 = (pointeur[0],pointeur[1]-hauteur_digit)
        arrivee3 = (arrivee1[0],debut3[1])
        segment(debut1,arrivee1,matrix,epaisseur)
        segment(debut2,arrivee2,matrix,epaisseur)
        segment(debut3,arrivee3,matrix,epaisseur)
        segment(arrivee2,arrivee1,matrix,epaisseur)
        segment(arrivee3,arrivee2,matrix,epaisseur)
        segment(debut3,debut2,matrix,epaisseur)
        segment(debut2,debut1,matrix,epaisseur)
        pointeur = arrivee1[0] + epaisseur*2,arrivee1[1]-epaisseur
        return pointeur
    elif number == 9:
        debut1 = pointeur
        arrivee1 = (debut1[0] + largeur_digit,debut1[1] + epaisseur)
        debut2 =( pointeur[0],pointeur[1]-hauteur_digit//2)
        arrivee2 = (arrivee1[0],debut2[1])
        debut3 = (pointeur[0],pointeur[1]-hauteur_digit)
        arrivee3 = (arrivee1[0],debut3[1])
        segment(debut1,arrivee1,matrix,epaisseur)
        segment(debut2,arrivee2,matrix,epaisseur)
        segment(debut3,arrivee3,matrix,epaisseur)
        segment(arrivee2,arrivee1,matrix,epaisseur)
        segment(arrivee3,arrivee2,matrix,epaisseur)
        segment(debut3,debut2,matrix,epaisseur)
        pointeur = arrivee1[0] + epaisseur*2,arrivee1[1]-epaisseur
        return pointeur
    else:
        debut1 = pointeur
        arrivee1 = (debut1[0] + largeur_digit,debut1[1] + epaisseur)
        debut2 =( pointeur[0],pointeur[1]-hauteur_digit//2)
        arrivee2 = (arrivee1[0],debut2[1])
        debut3 = (pointeur[0],pointeur[1]-hauteur_digit)
        arrivee3 = (arrivee1[0],debut3[1])
        segment(debut1,arrivee1,matrix,epaisseur)
        segment(debut3,arrivee3,matrix,epaisseur)
        segment(arrivee2,arrivee1,matrix,epaisseur)
        segment(arrivee3,arrivee2,matrix,epaisseur)
        segment(debut3,debut2,matrix,epaisseur)
        segment(debut2,debut1,matrix,epaisseur)
        pointeur = arrivee1[0] + epaisseur*2,arrivee1[1]-epaisseur
        return pointeur

def convert_coord(absx,ordy,taille_image):
    """convertit la coordée des points en coordoonée adaptée à l'image PPM"""
    pixelx,pixely = (absx+1)*((taille_image-1)/2), (1-ordy)*((taille_image-1)/2)
    if pixelx - int(pixelx) > 0.5:
        pixelx += 1
    if pixely - int(pixely) > 0.5:
        pixely += 1
    return int(pixelx),int(pixely)

def generate_ppm_file(taille_image,num_image,approx_pi,liste,matrix,liste_name,
hauteur_digit,longueur_digit,epaisseur,pointeur):
    """génère une image au format PPM"""
    approx_pi = approx_pi[0] + "-" + approx_pi[2:]
    name = f"img{num_image}_{approx_pi}.ppm"
    liste_name += [name]
    file = open(name,'w',encoding = 'utf-8')
    file.write("P3\n")
    file.write(f"{taille_image} {taille_image}\n")
    file.write("255 \n")
    for k in liste:
        pixelx,pixely = convert_coord(k[0],k[1],taille_image)
        if k[2]:
            matrix[pixely][pixelx] = "0 0 255 \n"
        else:
            matrix[pixely][pixelx] = "253 70 38 \n"
    matrix_copy = copy.deepcopy(matrix)
    pointeur = write_digit(int(approx_pi[0]),matrix,pointeur,epaisseur,hauteur_digit,longueur_digit)
    pointeur = point(matrix,pointeur,epaisseur)
    str_approx_pi = list(str(approx_pi[2:]))
    for k in str_approx_pi:
        pointeur = write_digit(int(k),matrix,pointeur,epaisseur,hauteur_digit,longueur_digit)
    for i in range(taille_image):
        for j in range(taille_image):
            file.write(matrix[i][j])
    file.close()
    return matrix_copy

def main():
    """gènère un GIF de la méthode Monté-Carlo"""
    entree = sys.argv
    taille_image, nb_points, chiffres_apres_virgule = entree[1],entree[2],entree[3]
    if len(entree) != 4:
        raise IndexError(" ./draw.py taille_image nb_point,chiffres_apres_virgule")
    elif (not taille_image.isdigit() or not chiffres_apres_virgule.isdigit()
    or not nb_points.isdigit()):
        raise ValueError("Erreur: il faut entrer 3 entiers")
    taille_image,nb_points = int(taille_image),int(nb_points)
    chiffres_apres_virgule = int(chiffres_apres_virgule)
    if nb_points < 100:
        raise ValueError("Le nombre de points doit être supérieur ou égale à 100")
    elif taille_image < 100:
        raise ValueError("la taille de l'image doit être supérieur ou égale à 100")
    elif not 1 <= chiffres_apres_virgule <= 5:
        raise ValueError("le nombre de chiffres après la virgule doit être compris entre 1 et 5")

    matrix = [["255 255 255\n"for _ in range(taille_image)] for _ in range(taille_image)]
    liste_name = []
    hauteur_digit,longueur_digit = taille_image//11, taille_image//22
    epaisseur = taille_image//200
    pointeur = (taille_image-(chiffres_apres_virgule+1)*longueur_digit)//2,(taille_image
    +hauteur_digit)//2
    liste,liste_approx_pi = approximate_pi.approxim_pi(nb_points)
    for k in range(len(liste_approx_pi)):
        approx_pi = f"{liste_approx_pi[k]:.{chiffres_apres_virgule}f}"
        matrix = generate_ppm_file(taille_image,k,approx_pi,
        liste[k*(nb_points//10):(k+1)*(nb_points//10)],matrix,liste_name,
        hauteur_digit,longueur_digit,epaisseur,pointeur)
    subprocess.run("convert -delay 100 -loop 0 img*.ppm img.gif",shell = True, check = True)

main()
