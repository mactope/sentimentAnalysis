# OOP programming to create ML model for sentiment analysis of articles
import nltk
from newspaper import Article
from textblob import TextBlob
from django.shortcuts import render


class articleSentiment():
    def __init__(self, url):
        self.url = url
        self.article = Article(url)
        self.article.download()
        self.article.parse()
        self.article.nlp()
        self.text = self.article.summary
        self.obj = TextBlob(self.text)
        self.sentiment = self.obj.sentiment.polarity
        print(self.sentiment)
        
    def generateSummary(self):
        return self.article.summary
        
    def predict(self):
        if self.sentiment == 0:
            prediction1 = "This is neutral"
        elif self.sentiment >0:
            prediction1 = "This is positive"
        else:
            prediction1 = "This is negative"
        return prediction1
    
#creating object of class
# url = 'https://www.theguardian.com/world/2022/apr/17/after-bucha-im-afraid-of-russian-soldiers-people-in-east-ukraine-prepare-for-fresh-assault'

# obj = articleSentiment(url)
# obj.predict()