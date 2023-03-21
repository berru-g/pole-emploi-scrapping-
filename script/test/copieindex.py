"""    
      Learn python 
      github/berru-g 23 
"""
import tkinter as tk
import time
import datetime
import requests
from bs4 import BeautifulSoup

root = tk.Tk()
root.title("Recherche d'emploi multiplatform en un click")
#root.iconbitmap('src\logo.png')
#p1 = tk.PhotoImage(file = 'src\logo.png')
#root.iconphoto(False, p1)
root.config(bg="#1d3557") 
title_color = "#1d3557"
subtitle_color = "#2a9d8f"
date_color = "#f4a261"

job_label = tk.Label(root, text="Rechercher métier:", foreground="#f1faee")
job_label.grid(row=1, column=0, padx=10, pady=10)
job_label.config(bg="#1d3557")
job_entry = tk.Entry(root)
job_entry.grid(row=0, column=1, padx=10, pady=10)

location_label = tk.Label(root, text="Lieux", foreground="#f1faee")
location_label.grid(row=0, column=0, padx=10, pady=10)
location_label.config(bg="#1d3557")
location_entry = tk.Entry(root)
location_entry.grid(row=1, column=1, padx=10, pady=10)

results_text = tk.Text(root)
font_style = ("Helvetica", 12)
#results_text = tk.Text(font=font_style, height=10, width=50)
results_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

def search():
    job = job_entry.get()
    location = location_entry.get()
    # search firstsite.com  # bug de la requete 'location', essaie d'inverser lieux et motcles comme dans lurl dorigine, puis change l'ordre de format, job, location= sans succes
    firstsite_url = "https://candidat.pole-emploi.fr/offres/recherche?&motsCles={}&lieux{}&offresPartenaires=true&rayon=10&tri=0" # 'location' not taken into account. because not "=" in url? 
    firstsite_search = requests.get(firstsite_url.format(job,location))
    firstsite_soup = BeautifulSoup(firstsite_search.text, "html.parser")
    firstsite_titles = firstsite_soup.find_all(class_="media-heading-title")
    subtitles = firstsite_soup.find_all(class_="subtext")
    dates = firstsite_soup.find_all(class_="date")
    results_text.delete('1.0', tk.END)  # Effacer le contenu de la zone de texte des résultats précédents
    results_text.insert(tk.END, "Résultats de la recherche sur Pole Emploi:\n\n", "blue")
    results_text.tag_configure("blue", foreground="#1d3557")
    for title, subtitle, date in zip(firstsite_titles, subtitles, dates):
        results_text.insert(tk.END, f"{title.text}\n", "title")
        results_text.insert(tk.END, f"{subtitle.text}\n", "subtitle")
        results_text.insert(tk.END, f"{date.text}\n", "date")
        results_text.insert(tk.END, "__________\n")
    # Applique les couleurs
    results_text.tag_config("title", foreground=title_color)
    results_text.tag_config("subtitle", foreground=subtitle_color)
    results_text.tag_config("date", foreground=date_color)
    print("resultat first site")
    time.sleep(1) 
    # Search secondsite.com
    secondsite_url ="https://www.jobijoba.com/fr/query/?what={}&where={}&where_type=city"               
    secondsite_search = requests.get(secondsite_url.format(job,location))
    secondsite_soup = BeautifulSoup(secondsite_search.text, "html.parser")
    secondsite_titles = secondsite_soup.find_all(class_="offer-header-title")
    secondsite_subtitles = secondsite_soup.find_all(class_="description")#md:tw-text-xlOld tw-text-2xlOld tw-leading-[1.625rem]
    secondsite_dates = secondsite_soup.find_all(class_="text-primary publication_date")
    results_text.insert(tk.END, "Résultats de la recherche jobijoba:\n\n", "blue")
    results_text.tag_configure("blue", foreground="#1d3557")
    for title, subtitle, date in zip(secondsite_titles, secondsite_subtitles, secondsite_dates):
        results_text.insert(tk.END, f"{title.text}\n", "title")
        results_text.insert(tk.END, f"{subtitle.text}\n", "subtitle")
        results_text.insert(tk.END, f"{date.text}\n", "date")
        results_text.insert(tk.END, "__________\n")
    print("resultat second site")
    time.sleep(1)   
    # Search thirdsite.com
    thirdsite_url ="https://fr.indeed.com/jobs?q={}&l={}"               
    thirdsite_search = requests.get(thirdsite_url.format(job,location))
    thirdsite_soup = BeautifulSoup(thirdsite_search.text, "html.parser")
    thirdsite_titles = thirdsite_soup.find_all(class_="jcs-JobTitle css-jspxzf eu4oa1w0")
    thirdsite_subtitles = thirdsite_soup.find_all(class_="heading6 company_location tapItem-gutter companyInfo")
    thirdsite_dates = thirdsite_soup.find_all(class_="new css-ud6i3y eu4oa1w0")
    results_text.insert(tk.END, "Résultats de la recherche indeed:\n\n", "blue")
    results_text.tag_configure("blue", foreground="#1d3557")
    for title, subtitle, date in zip(thirdsite_titles, thirdsite_subtitles, thirdsite_dates):
        results_text.insert(tk.END, f"{title.text}\n", "title")
        results_text.insert(tk.END, f"{subtitle.text}\n", "subtitle")
        results_text.insert(tk.END, f"{date.text}\n", "date")
        results_text.insert(tk.END, "__________\n")
    print("resultat third site")
    time.sleep(1)    
# Comparaison des dates
    if dates:
        latest_date = compare_dates(dates)
        print("La dernière date trouvée sur le site de recherche est:", latest_date)

    if secondsite_dates:
        latest_date = compare_dates(secondsite_dates)
        print("La dernière date trouvée sur le premier site est:", latest_date)

    if thirdsite_dates:
        latest_date = compare_dates(thirdsite_dates)
        print("La dernière date trouvée sur le troisième site est:", latest_date)
     
def compare_dates(date_list):
    
    latest_date = None
    for date_str in date_list:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        if latest_date is None or date > latest_date:
            latest_date = date
    return latest_date.strftime('%Y-%m-%d')

search_button = tk.Button(root, text="Rechercher", command=search)
search_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
