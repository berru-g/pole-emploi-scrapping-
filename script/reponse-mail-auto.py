import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Set up the email parameters
sender_email = "votre_adresse_email@gmail.com"
sender_password = "votre_mot_de_passe"
receiver_email = "adresse_email_du_destinataire@gmail.com"
mail_subject = "Candidature pour l'offre d'emploi"

# Send an HTTP request to the website
url = "https://candidat.pole-emploi.fr/offres/emploi/developpeur-web/nantes/s29m2v6"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find the link to the offer page
offer_link = soup.find("a", class_="media-heading-link")["href"]

# Send an HTTP request to the offer page
offer_response = requests.get(offer_link)

# Parse the HTML content of the offer page
offer_soup = BeautifulSoup(offer_response.text, "html.parser")

# Find the email of the recruiter
recruiter_email = offer_soup.find("a", {"href": "mailto:"})["href"].split(":")[1]

# Create the email message
mail_body = "Bonjour,\n\nJe vous écris pour vous proposer ma candidature pour l'offre d'emploi de développeur web à Nantes. Vous trouverez ci-joint mon CV.\n\nCordialement,\nGael-berru"
message = MIMEMultipart()
message.attach(MIMEText(mail_body, "plain"))
cv_attachment = MIMEApplication(open("chemin_vers_votre_cv.pdf", "rb").read(), _subtype="pdf")
cv_attachment.add_header("Content-Disposition", "attachment", filename="cv.pdf")
message.attach(cv_attachment)
message["Subject"] = mail_subject
message["From"] = sender_email
message["To"] = receiver_email

#
