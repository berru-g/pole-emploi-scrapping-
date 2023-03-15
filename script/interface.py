from pyautogui import sleep
import requests
from bs4 import BeautifulSoup
import tkinter as tk
# Create a new window
window = tk.Tk()
# Set the window title
window.title("Recherche d'emploi")

# Create input fields for job and location
job_label = tk.Label(window, text="Titre du poste:")
job_label.pack()
job_entry = tk.Entry(window)
job_entry.pack()

location_label = tk.Label(window, text="Emplacement:")
location_label.pack()
location_entry = tk.Entry(window)
location_entry.pack()

# Create a button to trigger the search
search_button = tk.Button(window, text="Rechercher")
search_button.pack()

# Create a text widget to display the results
results_text = tk.Text(window)
results_text.pack()

def search_jobs():
    # Get user input for job and location
    job = job_entry.get()
    location = location_entry.get()

    # Search Pole Emploi
    poleemploi_search = requests.get(poleemploi_url.format(job, location))
    poleemploi_soup = BeautifulSoup(poleemploi_search.text, "html.parser")
    poleemploi_titles = poleemploi_soup.find_all(class_="media-heading-title")

    # Display results for Pole Emploi
    results_text.insert(tk.END, "Résultats de la recherche sur Pole Emploi:\n")
    for title in poleemploi_titles:
        results_text.insert(tk.END, title.text + "\n")

    # Search Codeur.com
    codeur_search = requests.get(codeur_url.format(job, location))
    codeur_soup = BeautifulSoup(codeur_search.text, "html.parser")
    codeur_titles = codeur_soup.find_all(class_="card__title")

    # Display results for Codeur.com
    results_text.insert(tk.END, "\nRésultats de la recherche sur Codeur.com:\n")
    for title in codeur_titles:
        results_text.insert(tk.END, title.text.strip() + "\n")

    # Search Indeed.com
    indeed_search = requests.get(indeed_url.format(job, location))
    indeed_soup = BeautifulSoup(indeed_search.text, "html.parser")
    indeed_titles = indeed_soup.find_all(class_="jobtitle")

