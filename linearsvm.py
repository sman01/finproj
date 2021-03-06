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





