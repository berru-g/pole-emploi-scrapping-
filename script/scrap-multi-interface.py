"""    Learn python 
      github/berru-g 23
      scrp-multi-platform-V-1.0
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
    poleemploi_url = "https://candidat.pole-emploi.fr/offres/recherche?&motsCles={}&lieux{}&offresPartenaires=true&rayon=10&tri=0" # 'location' not taken into account. because not "=" in url? 
    jeudisdotcom_url = "https://www.lesjeudis.com/recherche?keywords={}&location={}"
    indeed_url = "https://fr.indeed.com/emplois?q={}&l={}&vjk=52ed5b81115cbba2"
    # search popol
    poleemploi_search = requests.get(poleemploi_url.format(job, location))
    poleemploi_soup = BeautifulSoup(poleemploi_search.text, "html.parser")
    poleemploi_titles = poleemploi_soup.find_all(class_="media-heading-title")
    subtitles = poleemploi_soup.find_all(class_="subtext")
    dates = poleemploi_soup.find_all(class_="date")
    # Search jeudisdotcom.com
    jeudisdotcom_search = requests.get(jeudisdotcom_url.format(job, location))
    jeudisdotcom_soup = BeautifulSoup(jeudisdotcom_search.text, "html.parser")
    jeudisdotcom_titles = jeudisdotcom_soup.find_all(class_=["data-results-title.dark-blue-text.b" , "data-results-content block job-listing-item"])
    #sub class
    #date class
    # Search Indeed.com
    indeed_search = requests.get(indeed_url.format(job, location))
    indeed_soup = BeautifulSoup(indeed_search.text, "html.parser")
    indeed_titles = indeed_soup.find_all(id_=["jobTitle-37b88858c4da5049","jobTitle css-1h4a4n5 eu4oa1w0"]) # [.,.] recup une class si l'autre n'existe pas. # [.,.] recup une class si l'autre n'existe pas.
    #sub class
    #date class
    
    results_text.delete('1.0', tk.END)  # Effacer le contenu de la zone de texte des résultats précédents
    
    results_text.insert(tk.END, "Résultats de la recherche sur Pole Emploi:\n\n")
    for title, subtitle, date in zip(poleemploi_titles, subtitles, dates):
        results_text.insert(tk.END, f"{title.text}\n{subtitle.text}\n{date.text}\n__________\n")
        
    results_text.insert(tk.END, "Résultats de la recherche les jeudis.com:\n\n")
    for title, subtitle, date in zip(jeudisdotcom_titles, subtitles, dates):
        results_text.insert(tk.END, f"{title.text}\n{subtitle.text}\n{date.text}\n__________\n")
        
    results_text.insert(tk.END, "Résultats de la recherche sur Indeed:\n\n")
    for title, subtitle, date in zip(indeed_titles, subtitles, dates):
        results_text.insert(tk.END, f"{title.text}\n{subtitle.text}\n{date.text}\n__________\n")

# Define the send function to send an email
def send():
    # Create the message object
    msg = MIMEMultipart()
    
    # Set the sender, recipient, and subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'recipient@example.com'
    msg['Subject'] = 'CV groupé'
    
    # Set the message body
    body = 'Bonjour,\n\nJe vous envoie mon CV pour postuler à des offres d\'emploi. Merci de prendre le temps de le consulter.\n\nCordialement,\n\nVotre nom'
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
    
    
root = tk.Tk()
root.title("Recherche d'emploi")
#root.iconbitmap(r'icon_1.ico')
#photo=PhotoImage(file="presentation.png")
root.config(bg="#457b9d")  # définit la couleur de fond en gris clair


job_label = tk.Label(root, text="Titre du poste")
job_label.grid(row=0, column=0, padx=10, pady=10)
job_entry = tk.Entry(root)
job_entry.grid(row=0, column=1, padx=10, pady=10)

location_label = tk.Label(root, text="Emplacement")
location_label.grid(row=1, column=0, padx=10, pady=10)
location_entry = tk.Entry(root)
location_entry.grid(row=1, column=1, padx=10, pady=10)

search_button = tk.Button(root, text="Rechercher", command=search)
search_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

send_button = tk.Button(root, text="Envoie CV groupé", command=send)
send_button.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

results_text = tk.Text(root)
results_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()