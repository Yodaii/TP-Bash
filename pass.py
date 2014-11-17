'''
Created on 13 nov. 2014

@author: Sohan
'''
from pip._vendor.distlib.compat import raw_input
import re


continuer = 1

while continuer == 1:
    passBon = 0
    
    while passBon == 0:
        mdp = raw_input("Quel est votre mot de passe?")
        aNbCar = len(mdp)
        aNombre = r"[0-9]"
        aCarSpec = r"[^0-9a-zA-Z]"
    
        if aNbCar < 8:
            print("Saisissez un mot de passe contenant au moins 8 caracteres.")
            aNbCar = len(mdp)
            continue
    
        if re.search(aNombre, mdp) is None:
            print("Saisissez un mot de passe avec un chiffre.")
            continue
    
        if re.search(aCarSpec, mdp) is None:
            print("Saisissez un mot de passe avec un caractere speciale.")
            continue
        
        passBon = 1
        
    continuer = int(input("Voulez-vous essayer un autre mot de passe? (1= Oui / 0= Non)"))