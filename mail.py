import smtplib

# Fournir les détails de l'expéditeur et du destinataire
from_addr = 'expéditeur@example.com'
to_addr = 'destinataire@example.com'

# Fournir les détails de connexion au serveur SMTP
smtp_server = 'smtp.example.com'
username = 'mon_nom_dutilisateur'
password = 'mon_mot_de_passe'

# Créer le contenu de l'e-mail
subject = 'Objet de l email'
body = 'Contenu de l email'

# Créer l'en-tête de l'e-mail
msg = f"Subject: {subject}\n\n{body}"

# Envoyer l'e-mail
server = smtplib.SMTP(smtp_server)
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, msg)
server.quit()