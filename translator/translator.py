import pandas as pd
from googletrans import Translator
from tqdm import tqdm
import string

# Load the CSV file
df = pd.read_csv('file.csv')

# Create a translator object
translator = Translator()

# Create a function to clean the text
def clean_text(text):
    # Remove unwanted characters and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    return text

# Iterate over the rows in the dataframe
for index, row in tqdm(df.iterrows(), total=df.shape[0]):
    comentario = row['comentario']
    comentario_ingles = ''

    # Check if the comment is in Portuguese
    if ' ' in comentario:
        # Translate the comment to English
        translation = translator.translate(comentario, src='pt', dest='en')
        comentario_ingles = translation.text

    # Clean the text
    comentario_ingles = clean_text(comentario_ingles)

    # Save the translated comment in the 'comentario_ingles' column
    df.at[index, 'comentario_ingles'] = comentario_ingles

    # Save the dataframe to a new CSV file after each iteration
    df.to_csv('reviews_final_ml_processed.csv', index=False)
