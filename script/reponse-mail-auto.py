import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Send an HTTP request to the website
url = "https://candidat.pole-emploi.fr/offres/emploi/developpeur-web/nantes/s29m2v6"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Find all the elements with class "product-title"
titles = soup.find_all(class_="media-heading-title")

# Find the email of the recruiter
email_elem = soup.find(class_="email-recruiter")
if email_elem:
    email = email_elem.text
else:
    email = None  # ou une autre valeur par défaut si nécessaire


# Create a message
msg = MIMEMultipart()
msg['From'] = 'g.leberruyer@gmail.com'  # Replace with your email address
msg['To'] = email
msg['Subject'] = 'Offre d\'emploi : ' + titles[0].text

# Add a message body
message = 'Bonjour,\n\nJe suis intéressé(e) par votre offre d\'emploi intitulée "' + titles[0].text + '". Pouvez-vous me fournir plus d\'informations ?\n\nCordialement,\nGithub.com/berru-g'
msg.attach(MIMEText(message))

# Connect to the SMTP server
smtp_server = 'smtp.gmail.com'  # Replace with the SMTP server of your email provider
smtp_port = 587  # Replace with the SMTP port of your email provider
username = "g.leberruyer"  # Replace with your email address
password = "mdp"  # Replace with your email password
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password) #bug sur la "réponse"

# Send the message
text = msg.as_string()
server.sendmail(username, email, text)

# Close the SMTP server
server.quit()

# Print the titles
for title in titles:
    print(title.text)
