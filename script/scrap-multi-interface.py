"""    Learn python 
      github/berru-g 23
      scrp-multi-platform-V-1.0
      A convertir en envoie de dossier pour location de logement, 
"""
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def search():
    job = job_entry.get()
    location = location_entry.get()
    #                https://candidat.pole-emploi.fr/offres/recherche?lieux=44109&motsCles=fullstack&offresPartenaires=true&range=0-19&rayon=10&tri=0
    firstsite_url = "https://candidat.pole-emploi.fr/offres/recherche?&motsCles={}&lieux{}&offresPartenaires=true&rayon=10&tri=0" # 'location' not taken into account. because not "=" in url? 
    secondsite_url = "https://www.lesjeudis.com/recherche?keywords={}&location={}"
    thirdsite_url = "https://fr.indeed.com/emplois?q={}&l={}"
    # search popol
    firstsite_search = requests.get(firstsite_url.format(job, location))
    firstsite_soup = BeautifulSoup(firstsite_search.text, "html.parser")
    firstsite_titles = firstsite_soup.find_all(class_="media-heading-title")
    subtitles = firstsite_soup.find_all(class_="subtext")
    dates = firstsite_soup.find_all(class_="date")
    # Search secondsite.com
    secondsite_search = requests.get(secondsite_url.format(job, location))
    secondsite_soup = BeautifulSoup(secondsite_search.text, "html.parser")
    secondsite_titles = secondsite_soup.find_all(class_="data-results-title dark-blue-text b")
    secondsite_subtitles = secondsite_soup.find_all(class_="data-details")
    secondsite_dates = secondsite_soup.find_all(class_="data-results-publish-time")
     
    # Search thirdsite.com
    thirdsite_search = requests.get(thirdsite_url.format(job, location))
    thirdsite_soup = BeautifulSoup(thirdsite_search.text, "html.parser")
    thirdsite_titles = thirdsite_soup.find_all(id_="jcs-JobTitle css-jspxzf eu4oa1w0") # [.,.] recup une class si l'autre n'existe pas. # [.,.] recup une class si l'autre n'existe pas.
    #sub class
    #date class
    
    results_text.delete('1.0', tk.END)  # Effacer le contenu de la zone de texte des résultats précédents
    results_text.insert(tk.END, "Résultats de la recherche sur Pole Emploi:\n\n")
    for title, subtitle, date in zip(firstsite_titles, subtitles, dates):
        results_text.insert(tk.END, f"{title.text}\n{subtitle.text}\n{date.text}\n__________\n")
        
    results_text.insert(tk.END, "Résultats de la recherche les jeudis.com:\n\n")
    for title, subtitle, date in zip(secondsite_titles, secondsite_subtitles, secondsite_dates):
        results_text.insert(tk.END, f"{title.text}\n{subtitle.text}\n{date.text}\n__________\n")
        
    results_text.insert(tk.END, "Résultats de la recherche sur thirdsite:\n\n")
    for title, subtitle, date in zip(thirdsite_titles, subtitles, dates):
        results_text.insert(tk.END, f"{title.text}\n{subtitle.text}\n{date.text}\n__________\n")

# Define the send function to send an email
def send():
    # Create the message object
    msg = MIMEMultipart()
"""    
    # changer/recuperer la class du btn d'envoie  - envoie pdf en scr du projet
    # Set the sender, recipient, and subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'recipient@example.com'
    msg['Subject'] = 'CV groupé'
    
    # Set the message body
    body = 'Bonjour,\n\nJe vous envoie mon CV pour postuler à votre offres d\'emploi. Merci de prendre le temps de le consulter.\n\nCordialement,\n\nVotre nom'
    msg.attach(MIMEText(body))
    
    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    # Login to the SMTP server
    server.login('your_email@example.com', 'your_email_password')
    
    # Send the email
    server.sendmail('your_email@example.com', 'recipient@example.com', msg.as_string())
    
    # Disconnect from the SMTP server
    server.quit()
"""    
    
root = tk.Tk()
root.title("Recherche d'emploi multiplatform en un click")
#root.iconbitmap(r'icon_1.ico')
#photo=PhotoImage(file="presentation.png")
root.config(bg="#457b9d")  # définit la couleur de fond en gris clair


job_label = tk.Label(root, text="Titre du poste")
job_label.grid(row=0, column=0, padx=10, pady=10)
job_entry = tk.Entry(root)
job_entry.grid(row=0, column=1, padx=10, pady=10)

location_label = tk.Label(root, text="Lieux")
location_label.grid(row=1, column=0, padx=10, pady=10)
location_entry = tk.Entry(root)
location_entry.grid(row=1, column=1, padx=10, pady=10)

search_button = tk.Button(root, text="Rechercher", command=search)
search_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

send_button = tk.Button(root, text="Envoie CV groupé", command=send)
send_button.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

results_text = tk.Text(root)
results_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
