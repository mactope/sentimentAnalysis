"""sentiment_analysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sLive/', views.sLive, name='sLive'),
    path('sTwitter/', views.sTwitter, name='sTwitter'),
    path('article_sentiment/', views.article_sentiment, name='article_sentiment'),
    path('sentimentUrl/', views.sentimentUrl, name='sentimentUrl'),
    path('nav/', views.nav, name='nav'),
    path('vaderResult/', views.vaderResult, name='vaderResult'),
    path('urlResult/', views.urlResult, name='urlResult'),
    path(('contact/'), views.contact, name='contact'),

]
