'''
Created on 13 nov. 2014

@author: Sohan
'''
from pip._vendor.distlib.compat import raw_input

# variable contenant le fichier passwd
fichier = open("passwd.txt", "r")

# Variable contenant toutes les lignes du fichier sous forme de liste
listLigne = [fichier.readline()] # ici on affecte uniquement la premiere ligne

# Variable permettant de se situer dans la liste
iterationLigne = 0

# Boucle While qui s'arrete quand on a parcouru toutes les lignes du fichier
while 1:
    listLigne.append(fichier.readline()) # ici on ajoute une ligne du fichier supplementaire a la liste
    # si la ligne ajouter est vide on sort de la boucle
    if listLigne[iterationLigne] == "":
        break
    # on icremente pour svoir combien de ligne contient le fichier et ne pas prendre en compte la ligne vide que le vient peut etre d ajouter
    iterationLigne = iterationLigne + 1
    
# on ferme le fichier apres que la lecture soit fini
fichier.close()

# variable contenant le nom entree par l utilisateur
nom = raw_input("Could you write the user name?")
# variable initialiser a vide qui contiendra les infos du nom
info = ""
# iteration i de la boucle while 
i = 0

# boucle while qui s'arrete lorsque l on a parcouru toutes la liste
while i != iterationLigne:
    # si le nom rentrer correspond a la premiere valeur de la chaine contenu a l emplacement i de la liste 
    # alors on recupere les informations du nom teste et on sort de la boucle
    if nom in listLigne[i].split(":")[0]:
        info = listLigne[i].split(":")
        break
    # sinon on incremente i et on recommence la boucle
    else:
        i = i + 1
 
# si la variable info est toujours vide ca signifie que le nom n est pas dans le fichier
# alors on le specifie q l utilisateur       
if info == "":
    print ("Error: " + nom + " is not an user name valid.")
# sinon on affiche les informations
else:
    print("The information asked is the following:")
    print("User Name: " + info[0])
    print("User Identifier: " + info[2])
    print("Group Identifier: " + info[3])
    if info[4] == "":
        print("Gecos Field: --")
    else:
        print("Gecos Field: " + info[4])
    print("Personal Directory: " + info[5])
    print("Shell: " + info[6])
    
