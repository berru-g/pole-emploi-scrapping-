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
url = "https://www.welcometothejungle.com/fr/jobs?groupBy=job&page=1&query=developpeur&sortBy=mostRelevant&aroundQuery=Nantes%2C%20France&aroundLatLng=47.21811%2C-1.55302&aroundRadius=20000" #caution: last url is 
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all the elements with class "product-title"
titles = soup.find_all(class_="sc-cwSeag-hlqow9-0-bOAYwm")
subtitles = soup.find_all(class_="sc-16yjgsd-0.haea-DT")
dates = soup.find_all(class_="sc-16yjgsd-0-haea-DT")

# Print the titles
for title in titles:
    for subtitle in subtitles:
        for date in dates:
            print(titles.text)
            print(subtitles.text)
            print(dates.text)
            
            
print("Fin des offres welcometothejungle.com")
sleep(1)

url = "https://www.lesjeudis.com/recherche?keywords=developpeur+web&location=nantes" #caution: last url is 
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all the elements with class "product-title"
titles = soup.find_all(class_="data-results-title")
subtitles = soup.find_all(class_="data-details")
date = soup.find_all(class_="block")

"""# Print the titles
for title in titles:
    for subtitles in subtitles:
        for date in date:
            print(title.text)
            print(subtitles.text)
            print(date.text)"""
for title in titles:
    print(titles.text)
            
print("Fin des offres les jeudis.com")
sleep(1)
exit()

"""#STEP 3
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
    print(offer_link.text)"""
    

