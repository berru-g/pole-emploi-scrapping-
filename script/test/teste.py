"""import os
import webbrowser

def open_private_browser(url):
    # Ouvre Firefox en mode privé
    firefox_path = "Program Files\Mozilla Firefox" # Modifier le chemin si nécessaire
    os.system(f"{firefox_path} -private-window {url}")

def launch_vpn():
    # Lance la connexion ProtonVPN
    protonvpn_path = "Program Files (x86)\Proton Technologies\ProtonVPN" # Modifier le chemin si nécessaire
    os.system(f"{protonvpn_path} connect")

print("Voulez-vous ouvrir une page web ?")

# Poser une question fermée avec une réponse par oui ou non
reponse_web = input()

# Afficher un message en fonction de la réponse
if reponse_web.lower() == "oui":
    # Demander l'URL de la page web à ouvrir
    print("Quelle est l'URL de la page web que vous souhaitez ouvrir ?")
    url = input()
    # Ouvrir la page web dans Firefox en mode privé et lancer ProtonVPN
    open_private_browser(url)
    launch_vpn()
elif reponse_web.lower() == "non":
    # Afficher un message si la réponse est "non"
    print("Vous avez choisi de ne pas ouvrir de page web.")
else:
    # Afficher un message si la réponse n'est ni "oui" ni "non"
    print("Je ne comprends pas votre réponse.")
"""
import tkinter as tk
import requests
from bs4 import BeautifulSoup

# Création de la fenêtre
root = tk.Tk()
root.geometry("600x400")
root.title("Résultats de recherche")

# Définition des couleurs
title_color = "#FF5733"
subtitle_color = "#900C3F"
date_color = "#C70039"

# Fonction pour récupérer les résultats de recherche
def get_results():
    # Efface le texte précédent
    results_text.delete("1.0", tk.END)

    # Récupère les résultats de recherche
    url = "https://www.lemonde.fr/recherche/?keywords=python"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("div", class_="SearchResults--item")

    # Affiche les résultats de recherche avec les couleurs spécifiées
    for result in results:
        title = result.find("h3", class_="ArticleItem--title")
        subtitle = result.find("div", class_="ArticleItem--excerpt")
        date = result.find("time", class_="ArticleItem--date")
        results_text.insert(tk.END, f"{title.text}\n", "title")
        results_text.insert(tk.END, f"{subtitle.text}\n", "subtitle")
        results_text.insert(tk.END, f"{date.text}\n", "date")
        results_text.insert(tk.END, "__________\n")
    
    # Applique les couleurs
    results_text.tag_config("title", foreground=title_color)
    results_text.tag_config("subtitle", foreground=subtitle_color)
    results_text.tag_config("date", foreground=date_color)

# Frame pour les résultats de recherche
results_frame = tk.Frame(root)
