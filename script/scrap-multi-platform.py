from pyautogui import sleep
import requests
from bs4 import BeautifulSoup

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

sleep(0.5)

# Search Codeur.com
codeur_search = requests.get(codeur_url.format(job, location))
codeur_soup = BeautifulSoup(codeur_search.text, "html.parser")
codeur_titles = codeur_soup.find_all(class_="card__title")

print("Résultats de la recherche sur Codeur.com:")
for title in codeur_titles:
    print(title.text.strip())

sleep(0.5)

# Search Indeed.com
indeed_search = requests.get(indeed_url.format(job, location))
indeed_soup = BeautifulSoup(indeed_search.text, "html.parser")
indeed_titles = indeed_soup.find_all(class_=["jobtitle", "title"]) # [.,.] recup une class si l'autre n'existe pas.

print("Résultats de la recherche sur Indeed.com:")
for title in indeed_titles:
    print(title.text)
    
print("Fin des résultats")
