# Analyse des Sentiments sur les Réseaux Sociaux

Ce script Python permet d'analyser les sentiments des commentaires provenant de publications Facebook et Instagram. L'analyse de sentiments est effectuée à l'aide de la bibliothèque NLTK (Natural Language Toolkit) et utilise les API officielles de Facebook ainsi que la bibliothèque Instaloader pour Instagram.

## Prérequis

Avant d'utiliser ce script, assurez-vous d'installer les dépendances nécessaires en utilisant la commande suivante :

    pip install facebook-sdk instaloader nltk

## Utilisation

  Remplacez les valeurs des variables facebook_post_id, facebook_access_token, instagram_post_url, instagram_username, et instagram_password par vos propres informations.

  Exécutez le script :

    python analyse-jo2024_nltks.py

## Résultats

Le script catégorise les commentaires en positifs, négatifs et neutres, puis fournit une synthèse pour le sujet donné (par exemple, "Jeux Olympiques Paris 2024").

## Avertissement

Assurez-vous de respecter les politiques d'utilisation des API de Facebook et d'Instagram. Le scraping direct peut violer les conditions d'utilisation des plateformes.
Licence

Ce projet est sous licence MIT.
