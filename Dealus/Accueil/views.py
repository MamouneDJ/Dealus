from django.shortcuts import render
from Annonce.models import Annonce
def home(request):
    vip_ads = Annonce.objects.filter(is_vip=True)
    allads = Annonce.objects.all()
    context = {
    'allads': allads.order_by('-date_ads_posted'),
    'vip_ads': vip_ads.order_by('-date_ads_posted'),
    }

    return render(request,'Accueil/home.html',context)


    