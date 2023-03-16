"""
Pratiquer cela dans des environnements de test pour éviter de bloquer votre ip.
from fake_useragent import UserAgent
STEP 1
change lieux={} &motscles={} et trouve toute les annonces
STEP 2
envoie mail auto
"""
from pyautogui import sleep 
import requests
from bs4 import BeautifulSoup
#STEP 1
# Send an HTTP request to the website // change lieux={} &motscles={}
in_url = "https://fr.indeed.com/jobs?q=d%C3%A9veloppeur+web&l=Rez%C3%A9+%2844%29&vjk=52ed5b81115cbba2" #caution: last in_url is 
in_response = requests.get(in_url)

# Parse the HTML content
soup = BeautifulSoup(in_response.text, "html.parser")

# Find all the elements with class "product-title"
in_titles = soup.find_all(class_="jcs-JobTitle css-jspxzf eu4oa1w0")
in_subtitles = soup.find_all(class_="turnstileLink companyOverviewLink")
date = soup.find_all(class_="date")

# Print the titles
for title in in_titles:
    for subtitles in in_subtitles:
        for date in date:
            print(title.text)
            print(in_subtitles.text)
            print(date.text)
            
print("Fin des offres")
    
    
"""
#STEP 3
send_url = "https://candidat.pole-emploi.fr/offres/emploi/developpeur-web/nantes/s29m2v6" #caution: last url is 
offer_response = requests.get(send_url)
# Find the link to the offer page
offer_link = soup.find("a", class_="media-heading-link")["href"]

# Send an HTTP request to the offer page
offer_response = requests.get(offer_link)

# Parse the HTML content of the offer page
offer_soup = BeautifulSoup(offer_response.text, "html.parser")

# Find the email of the recruiter
recruiter_email = offer_soup.find("a", {"href": "mailto:"})["href"].split(":")[1]

for offer_link in offer_link:
    print(offer_link.text)
    
"""
