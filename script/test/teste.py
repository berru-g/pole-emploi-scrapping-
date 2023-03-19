"""print("Bienvenue dans notre programme de question-réponse")

# Poser une question
print("Quel est votre nom?")
nom = input()

# Afficher la réponse
print("Bonjour, " + nom + "!")

# Poser une question avec plusieurs choix de réponses
print("Aimez-vous les chats ou les chiens?")
reponse = input()

# Afficher un message en fonction de la réponse
if reponse.lower() == "chats":
    print("Les chats sont géniaux!")
elif reponse.lower() == "chiens":
    print("Les chiens sont fantastiques!")
else:
    print("Je ne comprends pas votre réponse.")

# Poser une question fermée avec une réponse par oui ou non
print("Avez-vous déjà visité Paris?")
reponse = input()

# Afficher un message en fonction de la réponse
if reponse.lower() == "oui":
    print("Paris est une ville magnifique!")
elif reponse.lower() == "non":
    print("Vous devriez visiter Paris un jour!")
else:
    print("Je ne comprends pas votre réponse.")

# Fin du programme
print("Merci d'avoir utilisé notre programme de question-réponse.")"""

#############
import os

print("Voulez-vous ouvrir un fichier se trouvant dans votre dossier?")

# Poser une question fermée avec une réponse par oui ou non
reponse = input()

# Afficher un message en fonction de la réponse
if reponse.lower() == "oui":
    # Demander le nom du fichier à ouvrir
    print("Quel est le nom du fichier que vous souhaitez ouvrir?")
    nom_fichier = input()
    # Vérifier si le fichier existe
    if os.path.isfile(nom_fichier):
        # Ouvrir le fichier
        with open(nom_fichier, 'r') as f:
            contenu = f.read()
            print(contenu)
    else:
        # Afficher un message si le fichier n'existe pas
        print("Le fichier que vous avez entré n'existe pas.")
elif reponse.lower() == "non":
    # Afficher un message si la réponse est "non"
    print("Vous avez choisi de ne pas ouvrir de fichier.")
else:
    # Afficher un message si la réponse n'est ni "oui" ni "non"
    print("Je ne comprends pas votre réponse.")

