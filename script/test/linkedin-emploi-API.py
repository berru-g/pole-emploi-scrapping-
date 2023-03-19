from linkedin_api import LinkedIn

# initialisez l'API LinkedIn avec votre clé d'API et votre jeton d'accès
api = LinkedIn('v2', access_token='votre jeton d\'accès ici')
# définit les mots-clés à rechercher dans les annonces d'emploi
keywords = ['dev', 'front-end', 'développeur web']
# recherchez les annonces d'emploi avec les mots-clés spécifiés
jobs = api.search_jobs_v2(keywords=keywords)
# imprimez les résultats
for job in jobs:
    print(job['title'])
    print(job['descriptionSnippet'])
    print(job['jobPostingUrl'])
    # Envoyer une réponse automatique avec votre site Web
    message = f"Bonjour {job['companyName']}, je suis intéressé par le poste de {job['title']}. Pour en savoir plus sur mes compétences et mon expérience, veuillez consulter mon site Web {votre lien de site Web ici}"
    api.send_message_v2(recipient=job['listedJobPoster']['miniProfile'], message=message) 
# récupérer toutes les conversations liées à votre compte LinkedIn
conversations = api.get_conversations()
# filtrer les conversations avec les recruteurs
recruiter_conversations = [conv for conv in conversations if conv['entityUrn'].startswith('urn:li:fs_conversation:') and conv['participants'][0]['firstName'].lower() == 'recruiter']
# extraire les liens des annonces d'emploi correspondantes
for conv in recruiter_conversations:
    messages = api.get_conversation_messages_v2(conv['entityUrn'])
    for message in messages:
        if 'jobPostingUrl' in message:
            print(message['jobPostingUrl'])
