from django.shortcuts import render,redirect,get_object_or_404
from Annonce.models import Annonce
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def createAnnonce(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        owner= request.user
        fixed_p = request.POST.get('fixed_price')
        min_p = request.POST.get('min_price')
        max_p = request.POST.get('max_price')
        description = request.POST.get('description')
        abonnement = request.POST.get('abonnement')
        position = request.POST.get('position')
        is_vip = False
        if abonnement == 'vip':
            if owner.jetons - 500 >= 0:
                is_vip = True
                owner.jetons -= 500
                owner.save()
                print("reussi")
                print(f"il vous reste {owner.jetons}")
            else:
                return HttpResponse("va acheter des credits mec")
        #..........................
        annonce = Annonce(title=title, owner=owner,fixed_price=fixed_p,
                 min_price=min_p, max_price=max_p, description=description,is_vip=is_vip,latitude=coord[0],longitude=coord[1])
        annonce.save()
        return redirect('home')
    return render(request, 'Annonce/post_annonce.html')
def annonce_detail(request, slug):
    annonce = get_object_or_404(Annonce, slug=slug)
    return render(request, 'Annonce/annonce_detail.html', {'annonce': annonce})
@login_required
def user_ads(request):
    user_ads = request.user.annonce.all().order_by('-date_ads_posted')
    return render(request,'Annonce/user_ads.html',context={'user_ads':user_ads})
def edit_annonce(request,slug):
    annonce = get_object_or_404(Annonce, slug=slug)
    context = {'annonce':annonce,
               'position': str(annonce.latitude) + ',' + str(annonce.longitude)
               }
    if request.method == 'POST':
        title = request.POST.get('title')
        fixed_p = request.POST.get('fixed_price')
        min_p = request.POST.get('min_price')
        max_p = request.POST.get('max_price')
        description = request.POST.get('description')
        position = request.POST.get('position')
        annonce.title = title
        annonce.fixed_price = fixed_p
        annonce.min_price = min_p
        annonce.max_price = max_p
        annonce.description = description
        coord = position.split(',')
        annonce.latitude = coord[0]
        annonce.longitude = coord[1]
        annonce.save()
        return redirect('home')
    
    return render(request,'Annonce/edit_annonce.html',context)