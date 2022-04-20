#creating object oriented programming for sentiment analysis of sentence using vader
import nltk
#importing vader sentiment analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class sentimentVader():
    def __init__(self, sentence):
        self.sentence = sentence
        #creating object of vader sentiment analyzer
        self.sentiment_analyzer = SentimentIntensityAnalyzer()
        #predicting sentiment of sentence
        self.sentiment_dict = self.sentiment_analyzer.polarity_scores(self.sentence)
        

        
    def predict(self):
        if self.sentiment_dict['compound'] == 0:
            prediction = "This is neutral"
        elif self.sentiment_dict['compound'] >0:
            prediction = "This is positive"
        else:
            prediction = "This is negative"
        return prediction


#creating object of SentimentVader class
# sentence = "😢"
# obj= sentimentVader(sentence)
# obj.predict()


