#converting twitter sentiment analysis model into oop format
#importing
from tensorflow import keras 
import re
from keras.preprocessing.sequence import pad_sequences
from nltk.corpus import stopwords
from keras.models import load_model   # load saved model
from keras.preprocessing.text import Tokenizer
from nltk.corpus import stopwords
import tensorflow as tf



def twitter_prediction(review):
    import pickle
    model = tf.saved_model.load('D:/twitter_model.h5')
    regex = re.compile(r'[^a-zA-Z\s]')
    review = regex.sub('', review)
    print('Cleaned: ', review)

    # english stopwords
    english_stops = set(stopwords.words('english'))

    words = review.split(' ')
    filtered = [w for w in words if w not in english_stops]
    filtered = ' '.join(filtered)
    filtered = [filtered.lower()]

    #token
    token = Tokenizer()    
   

    max_length= 150; #based on stats of the data   
    


    tokenize_words = token.texts_to_sequences(filtered)
    tokenize_words = pad_sequences(tokenize_words, maxlen= max_length, padding='post', truncating='post')
    result = model.predict(tokenize_words)
    if result >= 0.7:
        print('positive')
    else:
        print('negative')
    

twitter_prediction('This is a very positive review')



# def sentiment_analysis(review):
#     #loading the trained model.
#     loaded_model = load_model('D:/twitter_model.h5')

#     regex = re.compile(r'[^a-zA-Z\s]')
#     review = regex.sub('', review)
#     print('Cleaned: ', review)

#     words = review.split(' ')
#     english_stops = set(stopwords.words('english'))
#     filtered = [w for w in words if w not in english_stops]
#     filtered = ' '.join(filtered)
#     filtered = [filtered.lower()]
    
#     tokenize_words = loaded_model.token.texts_to_sequences(filtered)
#     tokenize_words = pad_sequences(tokenize_words, maxlen=loaded_model.max_length, padding='post', truncating='post')
#     result = loaded_model.predict(tokenize_words)
#     print(result)
    
#     if result>0.7 :
#         print('positive')
   
#     else:
#         print("negative")


# sentiment_analysis('I love this movie')
    
    