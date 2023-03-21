"""    Learn python 
      github/berru-g 23
      scrp-multi-platform-V-1.0
      A convertir en envoie de dossier pour location de logement, 
"""
import tkinter as tk
import time
import requests
from bs4 import BeautifulSoup

def search():
    job = job_entry.get()
    location = location_entry.get()
    
    firstsite_url = "https://candidat.pole-emploi.fr/offres/recherche?&motsCles={}&lieux{}&offresPartenaires=true&rayon=10&tri=0" # 'location' not taken into account. because not "=" in url? 
    secondsite_url ="https://www.hellowork.com/fr-fr/emploi/recherche.html?k={}&l={}&l_autocomplete=&ray=20&msa=&d=all&c_idesegal="               
    thirdsite_url = "https://fr.indeed.com/emplois?q={}&l={}"
    # search firstsite.com  # bug de la requete 'location', essaie d'inverser lieux et motcles comme dans lurl dorigine, puis change l'ordre de format, job, location= sans succes
    firstsite_search = requests.get(firstsite_url.format(job,location))
    firstsite_soup = BeautifulSoup(firstsite_search.text, "html.parser")
    firstsite_titles = firstsite_soup.find_all(class_="media-heading-title")
    # Search secondsite.com
    secondsite_search = requests.get(secondsite_url.format(job,location))
    secondsite_soup = BeautifulSoup(secondsite_search.text, "html.parser")
    secondsite_titles = secondsite_soup.find_all(class_="tw-flex-tw-flex-wrap")   
    # Search thirdsite.com
    thirdsite_search = requests.get(thirdsite_url.format(job,location))
    thirdsite_soup = BeautifulSoup(thirdsite_search.text, "html.parser")
    thirdsite_titles = thirdsite_soup.find_all(class_="jcs-JobTitle-css-jspxzf-eu4oa1w0") # [.,.] recup une class si l'autre n'existe pas. # [.,.] recup une class si l'autre n'existe pas.
    #sub class
    #date class
    
    results_text.delete('1.0', tk.END)  # Effacer le contenu de la zone de texte des résultats précédents
    results_text.insert(tk.END, "Résultats de la recherche sur Pole Emploi:\n\n", "blue")
    results_text.tag_configure("blue", foreground="blue")
    for title in zip(firstsite_titles):
        results_text.insert(tk.END, f"{title.text}")
    time.sleep(1)
    results_text.insert(tk.END, "Résultats de la recherche les jeudis.com:\n\n", "blue")
    results_text.tag_configure("blue", foreground="blue")
    for title in zip(secondsite_titles):
        results_text.insert(tk.END, f"{title.text}")
    time.sleep(1)    
    results_text.insert(tk.END, "Résultats de la recherche sur Indeed:\n\n", "blue")
    results_text.tag_configure("blue", foreground="#1d3557")
    for title in zip(thirdsite_titles):
        results_text.insert(tk.END, f"{title.text}")
        


root = tk.Tk()
root.title("Recherche d'emploi multiplatform en un click")
#root.iconbitmap('src\logo.png')
p1 = tk.PhotoImage(file = 'src\logo.png')
root.iconphoto(False, p1)
root.config(bg="#1d3557")  # définit la couleur de fond en gris clair

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

search_button = tk.Button(root, text="Rechercher", command=search)
search_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


results_text = tk.Text(root)
results_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
