# Dans monapp/urls.py
from django.urls import path
from Annonce.views import createAnnonce

urlpatterns = [
    path('post/', createAnnonce, name='post'),
]
