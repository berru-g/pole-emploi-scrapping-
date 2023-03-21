"""    Learn python 
      github/berru-g 23
"""
#next step: use title, subtitle & date - ex: poleemploi.py
from pyautogui import sleep
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Get user input for job and location
print("Entrez le titre du poste:")
job = input("")
print("Entrez l emplacement:")
location = input("")

# URL templates for each site
#poleemploi_url = "https://candidat.pole-emploi.fr/offres/recherche?lieux={}&motsCles={}&offresPartenaires=true&rayon=10&tri=0"
poleemploi_url = "https://candidat.pole-emploi.fr/offres/recherche?&motsCles={}&lieux{}&offresPartenaires=true&rayon=10&tri=0"
jeudisdotcom_url = "https://www.lesjeudis.com/recherche?keywords={}&location={}&l_autocomplete=&ray=20&msa=&d=all&c_idesegal="
indeed_url = "https://fr.indeed.com/emplois?q={}&l={}&vjk="

# Search Pole Emploi
poleemploi_search = requests.get(poleemploi_url.format(job, location))
poleemploi_soup = BeautifulSoup(poleemploi_search.text, "html.parser")
poleemploi_titles = poleemploi_soup.find_all(class_="media-heading-title")
subtitles = poleemploi_soup.find_all(class_="subtext")
dates = poleemploi_soup.find_all(class_="date")

print("Résultats de la recherche sur Pole Emploi:")

# Print the titles
for title in poleemploi_titles:
    for subtitle in subtitles:
        for date in dates:
            print(title.text)
            print(subtitle.text)
            print(date.text)
            print("__________")

sleep(1)

# Search jeudisdotcom.com
jeudisdotcom_search = requests.get(jeudisdotcom_url.format(job, location))
jeudisdotcom_soup = BeautifulSoup(jeudisdotcom_search.text, "html.parser")
jeudisdotcom_titles = jeudisdotcom_soup.find_all(class_=["data-results-title.dark-blue-text.b" , "data-results-content block job-listing-item"])

print("Résultats de la recherche sur jeudis.com:")
for title in jeudisdotcom_titles:
    print(title.text)

sleep(1)
 
# Search Indeed.com
indeed_search = requests.get(indeed_url.format(job, location))
indeed_soup = BeautifulSoup(indeed_search.text, "html.parser")
indeed_titles = indeed_soup.find_all(id_=["jobTitle-37b88858c4da5049","jobTitle css-1h4a4n5 eu4oa1w0"]) # [.,.] recup une class si l'autre n'existe pas. # [.,.] recup une class si l'autre n'existe pas.

print("Résultats de la recherche sur Indeed.com:")
for title in indeed_titles:
    print(title.text)
    
sleep(1)

print("Fin des résultats")


print("Voulez-vous envoyer un mail groupé oui/non ?")

reponse = input()

# A refaire// inserer le script et non louvrir!!!

if reponse.lower() == "oui":
    # Lancer le script Python
    nom_script = "reponse-mail-auto.py" 
    if os.path.isfile(nom_script):
        os.system("python " + nom_script)
    else:
        # Afficher un message si le script n'existe pas
        print("Le script rencontre un probleme.")
              
elif reponse.lower() == "non":
    # Afficher un message si la réponse est "non" et quitter le programme
    print("Merci d'avoir utilisé notre programme.")
    print("Aidez nous à améliorer cet outil, rdv sur github.com/berru-g")
    exit()
