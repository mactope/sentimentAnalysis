 #making sentiment analysis model using LSTM trained model
import pickle
import re
import os

# Importing Keras library
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences




# Defining the function to make the sentiment analysis
def predict_sentiment(review):
    ModelPath = os.path.join(os.path.dirname(__file__), r"D:/UG/sentiment_analysis/sentiment_analysis/SentimentalAnalysis_LSTM.h5")
    # Loading the model
    model = load_model(ModelPath)
    #load tokenizer
    tokenizer = os.path.join(os.path.dirname(__file__), r"D:/UG/sentiment_analysis/sentiment_analysis/tokenizer.pickle")
    data = open(tokenizer, 'rb')
    tokenizer = pickle.load(data)
    # Cleaning the text
    regex = re.compile(r'[^a-zA-Z\s]')
    review = regex.sub('', review)
    preprocess = tokenizer.texts_to_sequences([review])
    preprocess=pad_sequences(preprocess,maxlen=500)
    prediction = model.predict(preprocess)
    prediction=prediction[0][1]
    
    if prediction >= 0.5:
        print('positive')
    else:
        print('negative')





#predict_sentiment('game is good')