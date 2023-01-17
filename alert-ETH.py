import requests
import smtplib

# API endpoint pour récupérer les données de prix de ETH
url = 'https://api.coinmarketcap.com/v1/ticker/ethereum/'

# Intervalle de temps pour vérifier le prix (en secondes)
interval = 60

while True:
    # Récupération des données de prix de ETH
    response = requests.get(url)
    data = response.json()[0]
    price = float(data['price_eur'])
    
    # Vérification si le prix de ETH est supérieur à 17000€
    if price > 17000:
        # Connexion au serveur SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("your_email@gmail.com", "your_password")
        
        # Envoi d'un email d'alerte
        subject = "Alerte de prix Ethereum"
        body = "Le prix de l'Ethereum a dépassé 17000€. Le cours actuel est de " + str(price) + "€"
        msg = f"Subject: {subject}\n\n{body}"
        server.sendmail("your_email@gmail.com", "receiver_email@gmail.com", msg)
        
        # Déconnexion du serveur SMTP
        server.quit()
        
        # Sortie de la boucle
        break
    else:
        # Attente avant de vérifier à nouveau le prix
        time.sleep(interval)
