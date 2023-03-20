import urllib
import pandas as pd
import bs4 
import requests

division=[]
equipe=[]
stade=[]
latitude_stade=[]        
longitude_stade=[]     

def dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    if direction == 'S' or direction == 'O':
        dd *= -1
    return dd

url_list=["http://fr.wikipedia.org/wiki/Championnat_de_France_de_football_2019-2020", "http://fr.wikipedia.org/wiki/Championnat_de_France_de_football_de_Ligue_2_2019-2020"]
url_ligue_1 = "https://fr.wikipedia.org/wiki/Championnat_de_France_de_football_2019-2020"
    
request_text = request.urlopen(url_ligue_1).read()
# print(request_text[:1000])    
type(request_text)

page = bs4.BeautifulSoup(request_text, "lxml")
print(page.find("title"))
print(page.find("table"))
print("Il y a", len(page.findAll("table")), "éléments dans la page qui sont des <table>")
# on identifie le tableau en question : c'est le premier qui a cette classe "wikitable sortable"
tableau_participants = page.find('table', {'class' : 'wikitable sortable'})
print(tableau_participants)
table_body = tableau_participants.find('tbody')
rows = table_body.find_all('tr')
print(rows[0])
print(rows[1])
cols = rows[1].find_all('td')
print(cols[0])
print(cols[0].text.strip())
for ele in cols : 
    print(ele.text.strip())
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    print(cols)


dico_participants = dict()
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    if len(cols) > 0 : 
        dico_participants[cols[0]] = cols[1:]
dico_participants


data_participants = pandas.DataFrame.from_dict(dico_participants,orient='index')
data_participants.head()


for row in rows:
    cols = row.find_all('th')
    print(cols)
    if len(cols) > 0 : 
        cols = [ele.get_text(separator=' ').strip().title() for ele in cols]
        columns_participants = cols


columns_participants


for url_ligue in url_list :
       
    print(url_ligue)
    sock = urllib.request.urlopen(url_ligue).read() 
    page=bs4.BeautifulSoup(sock)

# Rechercher les liens des équipes dans la liste disponible sur wikipedia 

    for team in page.findAll('span' , {'class' : 'toponyme'}) :  
        
        # Indiquer si c'est de la ligue 1 ou de la ligue 2
        
        if url_ligue==url_list[0] :
            division.append("L1")
        else :
            division.append("L2")

       # Trouver le nom et le lien de l'équipe
            
        if team.find('a')!=None :
            team_url=team.find('a').get('href')
            name_team=team.find('a').get('title')
            equipe.append(name_team)
            url_get_info = "http://fr.wikipedia.org"+team_url
            print(url_get_info)
 
       # aller sur la page de l'équipe
           
            search = urllib.request.urlopen(url_get_info).read()
            search_team=bs4.BeautifulSoup(search)

       # trouver le stade             
            compteur = 0
            for stadium in search_team.findAll('tr'):
                for x in stadium.findAll('th' , {'scope' : 'row'} ) :
                    if x.contents[0].string=="Stade" and compteur == 0:
                        compteur = 1
                        # trouver le lien du stade et son nom
                        url_stade=stadium.findAll('a')[1].get('href')
                        name_stadium=stadium.findAll('a')[1].get('title')
                        stade.append(name_stadium)
                        url_get_stade = "http://fr.wikipedia.org"+url_stade
                        print(url_get_stade)
                        
                        # Aller sur la page du stade et trouver ses coodronnées géographiques
                        
                        search_stade = urllib.request.urlopen(url_get_stade).read()
                        soup_stade=bs4.BeautifulSoup(search_stade) 
                        kartographer = soup_stade.find('a',{'class': "mw-kartographer-maplink"})
                        if kartographer == None :
                          latitude_stade.append(None)
                          longitude_stade.append(None) 
                        else :
                            for coordinates in kartographer :
                                print(coordinates)
                                liste =   coordinates.split(",")          
                                latitude_stade.append(str(liste[0]).replace(" ", "") + "'")
                                longitude_stade.append(str(liste[1]).replace(" ", "") + "'")
                            

dict = {'division' : division , 'equipe': equipe, 'stade': stade, 'latitude': latitude_stade, 'longitude' : longitude_stade}
data = pd.DataFrame(dict)
data = data.dropna()

data.head(5)

import re

def dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    if direction in ('S', 'O'):
        dd *= -1
    return dd

def parse_dms(dms):
    parts = re.split('[^\d\w]+', dms)
    lat = dms2dd(parts[0], parts[1], parts[2], parts[3])
    #lng = dms2dd(parts[4], parts[5], parts[6], parts[7])
    return lat


data['latitude'] = data['latitude'].apply(parse_dms)
data['longitude'] = data['longitude'].apply(parse_dms)


