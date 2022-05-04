from django.shortcuts import render
from django.http import HttpResponse
from numpy import character, var
from . import articleSentiment
from . import sentimentVader
from . import tweepy_sentiment
import mysql.connector as sql
from django.contrib import messages

fn = ''
ln=''
em=''
reg=''
sub=''




def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sLive(request):
    user_sentiment = str(request.GET.get('sentence'))
    obj= sentimentVader.sentimentVader(user_sentiment)
    prediction = obj.predict()  
    #only show result after the user has entered a sentence
    # also print the sentence and fade it after a few seconds

    if user_sentiment != '':
        return render(request, 'sLive.html', {'prediction': prediction, 'user_sentiment': user_sentiment})
    else:
        return render(request, 'sLive.html', {'prediction': 'Waiting.....'}) 
    


    
    

def sTwitter(request):
    return render(request, 'sTwitter.html')

def article_sentiment(request):
    return render(request, 'article_sentiment.html')

def sentimentUrl(request):
    return render(request, 'sentimentUrl.html')

def nav(request):
    return render(request, 'nav.html')

# def vaderResult(request):
#     user_sentiment = str(request.GET.get('sentence'))
#     obj= sentimentVader.sentimentVader(user_sentiment)
#     prediction = obj.predict()    
#     return render(request, 'vaderResult.html', {'prediction': prediction})

def urlResult(request):
    user_url = str(request.GET.get('url'))
    #handling the error if the url is not valid
    try:
        objArticle = articleSentiment.articleSentiment(user_url)
        prediction1 = objArticle.predict()
        summary = objArticle.generateSummary()
        return render(request, 'urlResult.html', {'prediction1': prediction1, 'summary': summary})
    except:
       #display error message as a visible message
        messages.error(request, 'Invalid URL')        
        
        return render(request, 'sentimentUrl.html')
        

        

    
    

def contact(request):
    global fn, ln, em, reg, sub
    if request.method == 'POST':
        m = sql.connect(host='localhost', user='root', password='root', database='users')
        cursor= m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == 'firstname':
                fn = value
            if key == 'lastname':
                ln = value
            if key == 'email':
                #validating the email
                if '@' in value and '.' in value:
                    em = value
                else:
                    messages.error(request, 'Invalid Email')
                    return render(request, 'contact.html')
            
            if key == 'region':
                reg = value
            if key == 'subject':
                sub = value
        c = "INSERT INTO users(firstname, lastname, region, subject, email) VALUES('"+fn+"', '"+ln+"', '"+em+"', '"+reg+"', '"+sub+"')"
        cursor.execute(c)
        m.commit()
        messages.success(request, 'Feedback/message submitted successfully')
        cursor.close()
    return render(request, 'contact.html')
def feature(request):
    return render(request, 'feature.html')

def message(request):
    return render(request, 'message.html')
    