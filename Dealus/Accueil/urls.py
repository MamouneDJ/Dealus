from django.urls import path
from Accueil.views import home
from Annonce.views import annonce_detail,edit_annonce,user_ads
urlpatterns = [
    path('',home,name='home'),
    path('annonces/',user_ads,name='user_ads'),
    path('annonce/<slug:slug>/', annonce_detail, name='annonce_detail'),
    path('modifier/<slug:slug>/',edit_annonce, name='edit_annonce')
]
