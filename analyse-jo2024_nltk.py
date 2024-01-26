import facebook
import instaloader
from nltk.sentiment import SentimentIntensityAnalyzer

def get_facebook_comments(post_id, access_token):
    # Fonction pour récupérer les commentaires depuis une publication Facebook
    graph = facebook.GraphAPI(access_token)
    comments = []

    try:
        # Récupérer les commentaires de la publication
        comments_data = graph.get_connections(post_id, 'comments')

        while 'data' in comments_data:
            # Ajouter les commentaires à la liste
            comments.extend(comment['message'] for comment in comments_data['data'])

            # Pagination des commentaires
            comments_data = graph.get_object(comments_data['paging']['next'])

    except facebook.GraphAPIError as e:
        print(f"Erreur lors de la récupération des commentaires Facebook : {e}")

    return comments

def get_instagram_comments(username, password, post_url):
    # Fonction pour récupérer les commentaires depuis une publication Instagram
    loader = instaloader.Instaloader()
    comments = []

    try:
        # Se connecter à Instagram
        loader.context.log_in(username, password)

        # Récupérer les commentaires de la publication
        post = instaloader.Post.from_shortcode(loader.context, post_url.split("/")[-2])
        comments = [comment.text for comment in post.get_comments()]

    except instaloader.exceptions.InstaloaderException as e:
        print(f"Erreur lors de la récupération des commentaires Instagram : {e}")

    return comments

def analyze_sentiments(comments):
    # Fonction pour analyser les sentiments des commentaires
    sia = SentimentIntensityAnalyzer()
    sentiments = [{'comment': comment, 'sentiment_score': sia.polarity_scores(comment)} for comment in comments]
    return sentiments

def categorize_sentiments(sentiments):
    # Fonction pour catégoriser les commentaires en fonction des sentiments
    compound_threshold = 0.05
    positive_comments = [comment['comment'] for comment in sentiments if comment['sentiment_score']['compound'] >= compound_threshold]
    negative_comments = [comment['comment'] for comment in sentiments if comment['sentiment_score']['compound'] <= -compound_threshold]
    neutral_comments = [comment['comment'] for comment in sentiments if -compound_threshold < comment['sentiment_score']['compound'] < compound_threshold]
    return positive_comments, negative_comments, neutral_comments

# Exemple d'utilisation
facebook_post_id = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  
facebook_access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  

instagram_post_url = 'https://www.instagram.com/joparis2024/'
instagram_username = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
instagram_password = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Récupérer les commentaires
facebook_comments = get_facebook_comments(facebook_post_id, facebook_access_token)
instagram_comments = get_instagram_comments(instagram_username, instagram_password, instagram_post_url)

# Analyser les sentiments
facebook_sentiments = analyze_sentiments(facebook_comments)
instagram_sentiments = analyze_sentiments(instagram_comments)

# Catégoriser les sentiments
positive_fb, negative_fb, neutral_fb = categorize_sentiments(facebook_sentiments)
positive_insta, negative_insta, neutral_insta = categorize_sentiments(instagram_sentiments)

# Synthèse pour le sujet "Jeux Olympiques 2024"
total_comments = len(facebook_comments) + len(instagram_comments)
total_positive = len(positive_fb) + len(positive_insta)
total_negative = len(negative_fb) + len(negative_insta)
total_neutral = len(neutral_fb) + len(neutral_insta)

print("\nSynthèse pour le sujet 'Jeux Olympiques 2024' :")
print(f"Total de commentaires : {total_comments}")
print(f"Nombre de commentaires positifs : {total_positive}")
print(f"Nombre de commentaires négatifs : {total_negative}")
print(f"Nombre de commentaires neutres : {total_neutral}")
