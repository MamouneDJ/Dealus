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
        coord = position.split(',')
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