from django.urls import path
from Accueil.views import home
from Annonce.views import annonce_detail
urlpatterns = [
    path('',home,name='home'),
    path('annonce/<int:annonce_id>/', annonce_detail, name='annonce_detail'),
]
