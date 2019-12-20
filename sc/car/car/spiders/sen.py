#textblob
import sys
import nltk
from importlib import reload
reload(sys)
sys.getdefaultencoding() # use this for Python3
from textblob import TextBlob
blob = TextBlob(open("analyse.txt").read())
print(blob.sentiment)
