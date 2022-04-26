from tensorflow import keras 
import re
from keras.preprocessing.sequence import pad_sequences
from nltk.corpus import stopwords
from keras.models import load_model   # load saved model
def twitter_sentiment(reviews):
    loaded_model = load_model('D:\UG\sentiment_analysis\sentiment_analysis\LSTM.h5')

    regex = re.compile(r'[^a-zA-Z\s]')
    review = regex.sub('', review)
    print('Cleaned: ', review)

    english_stops = set(stopwords.words('english'))

    words = review.split(' ')
    filtered = [w for w in words if w not in english_stops]
    filtered = ' '.join(filtered)
    filtered = [filtered.lower()]
    

    tokenize_words = token.texts_to_sequences(filtered)
    tokenize_words = pad_sequences(tokenize_words, maxlen=max_length, padding='post', truncating='post')
    print(tokenize_words)
    result = loaded_model.predict(tokenize_words)
    print(result)
    if result >= 0.7:
        print('positive')
    else:
        print('negative')