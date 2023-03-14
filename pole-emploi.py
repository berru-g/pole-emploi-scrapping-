import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the Pole Emploi job search page
url = "https://candidat.pole-emploi.fr/offres/recherche" # URL de la page de recherche
params = {'offresPartenaires': 'true', 'range': '0-9', 'rayon': '10', 'tri': '0', 'motsCles': 'dev front-end développeur web', 'lieux': '44'} 
#headers = {'User-Agent': 'Mozilla/5.0'}
#response = requests.get(url, headers=headers, params=params)
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all the job listings
job_listings = soup.find_all("li", class_="result")

# Print the job listings
for job_listing in job_listings:
    print(job_listings.text)
