'''
Created on 13 nov. 2014

@author: Sohan
'''
from pip._vendor.distlib.compat import raw_input
import re

# Condition de la boucle while
continuer = 1

# Boucle While permettant de recommencer l operation plusieurs fois tant que continuer vaut 1
while continuer == 1:
    # Valeur permettant d'indiquer que le pass est correct (condition d'arret)
    passBon = 0
    
    # Boucle While permettant de restester un mot de pass tant qu'un n'est pas correct
    while passBon == 0:
        mdp = raw_input("Quel est votre mot de passe?") # variable contenant le mot de passe
        aNbCar = len(mdp) # variable contenant la longueure du mot de passe
        aNombre = r"[0-9]" 
        aCarSpec = r"[^0-9a-zA-Z]"
    
        # Test si le mot de passe contient au moins 8 caracteres
        if aNbCar < 8:
            print("Saisissez un mot de passe contenant au moins 8 caracteres.")
            aNbCar = len(mdp)
            continue #permet de retourner au debut de la boucle
    
        # Test si le mot de passe contient au moins 1 chiffre
        if re.search(aNombre, mdp) is None:
            print("Saisissez un mot de passe avec un chiffre.")
            continue #permet de retourner au debut de la boucle
    
        # Test si le mot de pass contient au moins 1 caractre speciale
        if re.search(aCarSpec, mdp) is None:
            print("Saisissez un mot de passe avec un caractere speciale.")
            continue #permet de retourner au debut de la boucle
        
        # si tout les tests sont verifier, le mot de passe est correct, on sort de la boucle
        passBon = 1
        
    #permet de savoir si l'utilisateur veux recommencer
    continuer = int(input("Voulez-vous essayer un autre mot de passe? (1= Oui / 0= Non)"))