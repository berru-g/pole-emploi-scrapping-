"""    Learn python 
      github/berru-g 23
"""
from pyautogui import sleep
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
#from script-otto import reponse-mail-auto

# Get user input for job and location
print("Entrez le titre du poste:")
job = input("")
print("Entrez l emplacement:")
location = input("")

# URL templates for each site
#poleemploi_url = "https://candidat.pole-emploi.fr/offres/recherche?lieux={}&motsCles={}&offresPartenaires=true&rayon=10&tri=0"
poleemploi_url = "https://candidat.pole-emploi.fr/offres/recherche?&motsCles={}&lieux{}&offresPartenaires=true&rayon=10&tri=0"
codeur_url = "https://www.codeur.com/projects?query={}&location={}"
indeed_url = "https://fr.indeed.com/emplois?q={}&l={}"

# Search Pole Emploi
poleemploi_search = requests.get(poleemploi_url.format(job, location))
poleemploi_soup = BeautifulSoup(poleemploi_search.text, "html.parser")
poleemploi_titles = poleemploi_soup.find_all(class_="media-heading-title")

print("Résultats de la recherche sur Pole Emploi:")

for title in poleemploi_titles:
    print(title.text)
    

"""print("Résultats de la recherche sur Pole Emploi:")
print(poleemploi_search.content)
for title in poleemploi_titles:
    print(title.find(class_="title").text)"""

sleep(1)

# Search Codeur.com
codeur_search = requests.get(codeur_url.format(job, location))
codeur_soup = BeautifulSoup(codeur_search.text, "html.parser")
codeur_titles = codeur_soup.find_all(class_="card__title")

print("Résultats de la recherche sur Codeur.com:")
for title in codeur_titles:
    print(title.text.strip())

sleep(1)

# Search Indeed.com
indeed_search = requests.get(indeed_url.format(job, location))
indeed_soup = BeautifulSoup(indeed_search.text, "html.parser")
indeed_titles = indeed_soup.find_all(class_=["jobTitle css-1h4a4n5 eu4oa1w0", "jcs-JobTitle.css-jspxzf.eu4oa1w0"]) # [.,.] recup une class si l'autre n'existe pas.
#indeed_titles = indeed_soup.find_all(class_="jcs-JobTitle.css-jspxzf.eu4oa1w0") # [.,.] recup une class si l'autre n'existe pas.

print("Résultats de la recherche sur Indeed.com:")
for title in indeed_titles:
    print(title.text)
    
sleep(1)

print("Fin des résultats")


print("Voulez-vous envoyer un mail groupé oui/non ?")

reponse = input()

# Afficher un message en fonction de la réponse
if reponse.lower() == "oui":
    # Ouvrir le fichier
    nom_fichier = "reponse-mail-auto.py" 
    with open(nom_fichier, 'r') as f:
        contenu = f.read()
        print(contenu)
elif reponse.lower() == "non":
    # Afficher un message si la réponse est "non" et quitter le programme
    print("Merci d'avoir utilisé notre programme.")
    exit()
else:
    # Afficher un message si la réponse n'est ni "oui" ni "non"
    print("Aidez nous à améliorer cet outils, rdv sur github.com/berru-g")
