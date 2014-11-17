'''
Created on 13 nov. 2014

@author: Sohan
'''
from pip._vendor.distlib.compat import raw_input

fichier = open("passwd.txt", "r")
iterationLigne = 0
listLigne = [fichier.readline()]

while 1:
    listLigne.append(fichier.readline())
    if listLigne[iterationLigne] == "":
        break
    iterationLigne = iterationLigne + 1
    
print(listLigne)
fichier.close()

nom = raw_input("Could you write the user name?")
info = ""
 
i = 0
while i != iterationLigne:
    if nom in listLigne[i].split(":")[0]:
        info = listLigne[i].split(":")
        break
    else:
        i = i + 1
        
if info == "":
    print ("Error: " + nom + " is not an user name valid.")
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
    
