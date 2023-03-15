from pyautogui import sleep
import requests
from bs4 import BeautifulSoup

# Get user input for job and location
job = input("Entrez le titre du poste: ")
location = input("Entrez l'emplacement: ")

# URL templates for each site
#poleemploi_url = "https://candidat.pole-emploi.fr/offres/emploi/&job={}/&location={}/"  # probleme avec un code aléatoire en fin d'url
poleemploi_url = "https://candidat.pole-emploi.fr/offres/recherche?lieux={}&motsCles={}&offresPartenaires=true&rayon=10&tri=0"   
# &{}.format(lieux, mots_cles, identifiant)"
#https://candidat.pole-emploi.fr/offres/recherche?lieux=44109&motsCles=fullstack&offresPartenaires=true&rayon=10&tri=0
codeur_url = "https://www.codeur.com/projects?query={}&location={}"
indeed_url = "https://fr.indeed.com/emplois?q={}&l={}"

# Search Pole Emploi
#poleemploi_search = requests.get(poleemploi_url.format(job, location))
poleemploi_search = requests.get(poleemploi_url)
poleemploi_soup = BeautifulSoup(poleemploi_search.text, "html.parser")
poleemploi_titles = poleemploi_soup.find_all(class_="media-heading-title")

print("Résultats de la recherche sur Pole Emploi:")
for title in poleemploi_titles:
    print(title.text)

sleep(2)

# Search Codeur.com
codeur_search = requests.get(codeur_url.format(job, location))
codeur_soup = BeautifulSoup(codeur_search.text, "html.parser")
codeur_titles = codeur_soup.find_all(class_="card__title")

print("Résultats de la recherche sur Codeur.com:")
for title in codeur_titles:
    print(title.text.strip())

# Search Indeed.com
indeed_search = requests.get(indeed_url.format(job, location))
indeed_soup = BeautifulSoup(indeed_search.text, "html.parser")
indeed_titles = indeed_soup.find_all(class_="jobtitle")

print("Résultats de la recherche sur Indeed.com:")
for title in indeed_titles:
    print(title.text.strip())
