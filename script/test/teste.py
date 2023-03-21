import os
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
