import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk.data
from sklearn import preprocessing
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
#nltk.download()



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
print('Review')
print(df.Review)






def identify_tokens(row):
    Review = row['Review']
    tokens = nltk.word_tokenize(Review)
   # taken only words (not punctuation)
    token_words = [w for w in tokens if w.isalpha()]
    return token_words

df['words'] = df.apply(identify_tokens, axis=1)





stops = set(stopwords.words("english"))                  

def remove_stops(row):
    my_list = row['words']
    meaningful_words = [w for w in my_list if not w in stops]
    return (meaningful_words)

df['Review1'] = df.apply(remove_stops, axis=1)

print(df.Review1)

from nltk import pos_tag

from nltk.corpus import wordnet
def actpos(row):
    a=pos_tag(row)
    print (a)
    tag = pos_tag([a[1]])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

def pos(row):
    my_list=row['Review1']
   
    a=[get_wordnet_pos(word) for word in my_list]

    return(a)


print("'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
    
df['pos_tagged'] = df.apply(pos, axis=1)
print(df.pos_tagged)








            
        
 

'''
def stem_list(row):
    stemming=PorterStemmer()
    my_list = row['Review1']
    #print(my_list)
    stemmed_list = [stemming.stem(word) for word in my_list]
    return (stemmed_list)

df['stemmed_words'] = df.apply(stem_list, axis=1)
print("yoooooooooooo")
<<<<<<< HEAD
#print(df.stemmed_words)

=======
print(df.stemmed_words)
'''
from nltk.stem import WordNetLemmatizer



import nltk
    
   
def lema(row):
    lemming=WordNetLemmatizer()

    my_list=row['Review1']
    my_pos=row['pos_tagged']

    lemming_list=[lemming.lemmatize(w,p)for (w,p) in zip(my_list,my_pos)]

    #print (lemming_list)
    return (lemming_list)
df['lemmatized_words'] = df.apply(lema, axis=1)
#a=lema()
print("sfbfqbuiq")
print(df.lemmatized_words)

#df['lemmed_words'] = df.apply(lema, axis=1)
#print(df.lemmed_words)
#print(df.lemmed_words)'''

#print ("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word)))








def rejoin_words(row):
    my_list = row['lemmatized_words']
    joined_words = ( " ".join(my_list))
    return joined_words

df['processed'] = df.apply(rejoin_words, axis=1)



del df['Review']
del df['words']
#del df['stemmed_words']
#del df['lemmatized_words']
#del df['lemmed_words']



df.to_csv('df_processed.csv', index=False)




le = preprocessing.LabelEncoder()
df['Sentiment'] = le.fit_transform(df.Sentiment.values)
print(df.Sentiment)

X_tr = df.loc[:58, 'processed'].values
y_train = df.loc[:58, 'Sentiment'].values
X_te = df.loc[59:, 'processed'].values
y_test = df.loc[59:, 'Sentiment'].values


from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_tr)
X_test = vectorizer.transform(X_te)

#print(train_vectors.shape, test_vectors.shape)


    

#print(df)


#Create a svm Classifier
clf = svm.SVC(kernel='linear') # Linear Kernel

#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))


print("Precision:",metrics.precision_score(y_test, y_pred))

# Model Recall: what percentage of positive tuples are labelled as such?
print("Recall:",metrics.recall_score(y_test, y_pred))





