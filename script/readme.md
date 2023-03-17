### VERIFIER REQUETES HTTP

#### Voici les étapes pour installer et utiliser Postman :

    #### Téléchargez et installez Postman depuis [le site officiel :](https://www.postman.com/downloads/)

    #### Une fois que Postman est installé, ouvrez l'application et créez un nouvel onglet en cliquant sur le bouton "New".

    #### Dans la barre d'adresse, entrez l'URL de la page que vous souhaitez scrapper. Par exemple, pour tester l'URL de Codeur.com, vous pouvez entrer : https://www.codeur.com/projects?query=python&location=paris

    #### Choisissez la méthode HTTP appropriée pour votre requête. Pour récupérer du contenu HTML, utilisez la méthode GET.

    #### Cliquez sur le bouton "Send" pour envoyer la requête à la page web. Vous devriez voir la réponse de la page s'afficher dans la section "Response" de Postman.

    #### Si la réponse de la page est vide ou non valide, il se peut qu'il y ait un problème avec l'URL de la requête ou que le site web ne permette pas le scraping. Vous pouvez essayer de changer l'URL de la requête ou de vérifier les paramètres d'autorisation pour le site web.

    #### Si la réponse de la page est valide, vous pouvez utiliser les informations de réponse pour déterminer comment extraire les données que vous souhaitez scraper. Par exemple, vous pouvez utiliser les outils de Postman pour inspecter les éléments HTML de la page, les classes CSS, les identifiants et autres informations utiles pour extraire les données de la page à l'aide de votre script Python.