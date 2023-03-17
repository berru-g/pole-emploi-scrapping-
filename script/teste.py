
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
in_titles = soup.find(class_="jcs-JobTitle")
in_subtitles = soup.find(class_="subtext")
date = soup.find(class_="date")

# Print the titles
for title in in_titles:
    for subtitles in in_subtitles:
        for date in date:
            print(in_titles.text)
            print(in_subtitles.text)
            print(date.text)
            
print("Fin des offres")
    
    
