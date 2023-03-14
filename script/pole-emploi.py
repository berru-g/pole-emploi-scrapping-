"""
Pratiquer cela dans des environnements de test pour éviter de bloquer votre ip.
from fake_useragent import UserAgent

"""
import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the website
url = "https://candidat.pole-emploi.fr/offres/emploi/developpeur-web/nantes/s29m2v6"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all the elements with class "product-title"
titles = soup.find_all(class_="media-heading-title")

# Print the titles
for title in titles:
    print(title.text)
