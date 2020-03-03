import pandas as pd
import numpy as np
import re
import warnings
from bs4 import BeautifulSoup
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import seaborn as sns
import nltk.data

from nltk.tokenize import word_tokenize
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.feature_extraction.text import CountVectorizer



ds=pd.read_csv("output_1.csv",)



df = pd.DataFrame(ds)



exclude = set(string.punctuation)
def remove_punctuation(x):
    """
    Helper function to remove punctuation from a string
    x: any string
    """
    try:
        x = ''.join(ch for ch in x if ch not in exclude)
    except:
        pass
    return x
# Apply the function to the DataFrame
df.Review = df.Review.apply(remove_punctuation)



def identify_tokens(row):
    Review = row['Review']
    tokens = nltk.word_tokenize(Review)
   # taken only words (not punctuation)
    token_words = [w for w in tokens if w.isalpha()]
    return token_words

df['words'] = df.apply(identify_tokens, axis=1)





def stem_list(row):
    stemming=PorterStemmer()
    my_list = row['words']
    stemmed_list = [stemming.stem(word) for word in my_list]
    return (stemmed_list)

df['stemmed_words'] = df.apply(stem_list, axis=1)






from nltk.corpus import stopwords
stops = set(stopwords.words("english"))                  

def remove_stops(row):
    my_list = row['stemmed_words']
    meaningful_words = [w for w in my_list if not w in stops]
    return (meaningful_words)

df['stem_meaningful'] = df.apply(remove_stops, axis=1)






def rejoin_words(row):
    my_list = row['stem_meaningful']
    joined_words = ( " ".join(my_list))
    return joined_words

df['processed'] = df.apply(rejoin_words, axis=1)



del df['Review']
del df['words']
del df['stemmed_words']
del df['stem_meaningful']




df.to_csv('df_processed.csv', index=False)


#columns_titles = ["Sentiment","processed"]
#df=df.reindex(columns=columns_titles)

print(df)