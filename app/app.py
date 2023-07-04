import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer



# Read the CSV files
amazon_reviews = pd.read_csv('reviews_amazon_english_nowarning_final.csv')
mercadolivre_reviews = pd.read_csv('reviews_meli_english_nowarning_final.csv')

# Function to calculate sentiment scores
def calculate_sentiment_scores(df):
    sid = SentimentIntensityAnalyzer()
    df['Negativo'] = df['comentario_ingles'].apply(lambda x: sid.polarity_scores(x)['neg'] if isinstance(x, str) else np.nan)
    df['Positivo'] = df['comentario_ingles'].apply(lambda x: sid.polarity_scores(x)['pos'] if isinstance(x, str) else np.nan)
    df['Neutro'] = df['comentario_ingles'].apply(lambda x: sid.polarity_scores(x)['neu'] if isinstance(x, str) else np.nan)
    df['Nota'] = (df['Positivo'] + 0.5*df['Neutro']) * 100
    return df

# List of items
items = ['smartphone', 'smart tv', 'smart tv box', 'disco', 'console de videogame', 'fones de ouvido sem fio',
         'camera digital', 'tablet', 'smartwatch', 'joias', 'impressora', 'monitor', 'ssd', 'drone',
         'caixa de som portatil', 'aparelho de barbear eletrico', 'relogio', 'social', 'oculos', 'teclado',
         'mouse', 'maquina de cafe expresso', 'liquidificador', 'fritadeira', 'air fryer', 'aspirador',
         'ferro de passar roupa', 'chapinha de cabelo', 'maquina', 'purificador de ar', 'ventilador',
         'ar-condicionado portatil', 'cadeira de escritorio', 'mochila', 'bolsa', 'tenis', 'calca jeans',
         'sapatos sociais masculinos', 'mocassim', 'camiseta basica', 'vestido', 'perfume importado', 'tapete']

# Get user input for the item selection
selected_item = input("Select an item from the list: ")

# Filter the reviews based on the selected item
amazon_filtered_reviews = amazon_reviews[amazon_reviews['pesquisa'] == selected_item].copy()
mercadolivre_filtered_reviews = mercadolivre_reviews[mercadolivre_reviews['pesquisa'] == selected_item].copy()

# Calculate sentiment scores for both datasets
amazon_filtered_reviews = calculate_sentiment_scores(amazon_filtered_reviews)
mercadolivre_filtered_reviews = calculate_sentiment_scores(mercadolivre_filtered_reviews)

# Calculate average sentiment scores
amazon_average_score = amazon_filtered_reviews['Nota'].mean()
mercadolivre_average_score = mercadolivre_filtered_reviews['Nota'].mean()

# Get the comments with the lowest and highest scores for Amazon
amazon_lowest_score_comment = amazon_filtered_reviews.loc[amazon_filtered_reviews['Nota'].idxmin(), 'comentario']
amazon_highest_score_comment = amazon_filtered_reviews.loc[amazon_filtered_reviews['Nota'].idxmax(), 'comentario']

# Get the comments with the lowest and highest scores for Mercado Livre
mercadolivre_lowest_score_comment = mercadolivre_filtered_reviews.loc[mercadolivre_filtered_reviews['Nota'].idxmin(), 'comentario']
mercadolivre_highest_score_comment = mercadolivre_filtered_reviews.loc[mercadolivre_filtered_reviews['Nota'].idxmax(), 'comentario']

# Function to truncate comments if they exceed the specified length
def truncate_comment(comment, length=100):
    if len(comment) > length:
        return comment[:length] + '...'
    else:
        return comment

# Print the comparison and comments
print("Comparison between Amazon and Mercado Livre for item:", selected_item)
print("Amazon average score:", amazon_average_score)
print("Mercado Livre average score:", mercadolivre_average_score)
print("Amazon lowest score comment:", truncate_comment(amazon_lowest_score_comment))
print("Amazon highest score comment:", truncate_comment(amazon_highest_score_comment))
print("Mercado Livre lowest score comment:", truncate_comment(mercadolivre_lowest_score_comment))
print("Mercado Livre highest score comment:", truncate_comment(mercadolivre_highest_score_comment))