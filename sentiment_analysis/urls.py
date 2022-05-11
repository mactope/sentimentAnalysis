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
    path('sentimentUrl/', views.sentimentUrl, name='sentimentUrl'),    
    path('urlResult/', views.urlResult, name='urlResult'),
    path(('contact/'), views.contact, name='contact'),
    path(('feature/'), views.feature, name='feature'),  
    path(('sentiment_import/'), views.sentiment_import, name='sentiment_import'),
    path(('sentiment_import_result/'), views.sentiment_import_result, name='sentiment_import_result'),
    path(('sentiment_import_result_hashtag/'), views.sentiment_import_result_hashtag, name='sentiment_import_result_hashtag'),
    
   
    

]
