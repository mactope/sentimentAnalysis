from django.shortcuts import render
from django.http import HttpResponse
from numpy import character, var
from . import articleSentiment
from . import sentimentVader
from . import tweepy_sentiment





def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sLive(request):
    #user_input = request.GET.get('sentence')
    #prediction = sentimentVader.sentiment_score(user_input)
    return render(request, 'sLive.html')
    

def sTwitter(request):
    return render(request, 'sTwitter.html')

def article_sentiment(request):
    return render(request, 'article_sentiment.html')

def sentimentUrl(request):
    return render(request, 'sentimentUrl.html')

def nav(request):
    return render(request, 'nav.html')

def vaderResult(request):
    user_sentiment = str(request.GET.get('sentence'))
    obj= sentimentVader.sentimentVader(user_sentiment)
    prediction = obj.predict()
    return render(request, 'vaderResult.html', {'prediction': prediction})

def urlResult(request):
    user_url = str(request.GET.get('url'))
    objArticle= articleSentiment.articleSentiment(user_url)
    prediction1 = objArticle.predict()
    summary = objArticle.generateSummary()
    return render(request, 'urlResult.html', {'prediction1': prediction1, 'summary': summary})
    

def contact(request):
    return render(request, 'contact.html')