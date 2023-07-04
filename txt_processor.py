import pandas as pd
import numpy as np
from textblob import TextBlob
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re
from googletrans import Translator


def SentAnal(row):
    text = row['comentarios']

    tradutor = Translator(service_urls=['translate.google.com'])
    traducao = tradutor.translate(text, src='pt', dest='en').text
    traducao = re.sub("[^a-zA-Z']", " ", traducao)
    analisador = SentimentIntensityAnalyzer()
    scores = analisador.polarity_scores(traducao)
    neg = scores['neg']
    pos = scores['pos']
    neu = scores['neu']

    row['Traducao'] = traducao
    row['Negativo'] = neg
    row['Positivo'] = pos
    row['Neutro'] = neu
    row['Nota'] = (pos+neu)*100

    return row