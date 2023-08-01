from django.shortcuts import render
# Create your views here.
# Dans monapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Effectuez ici des vérifications supplémentaires, si nécessaire

        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        return redirect('login')
    return render(request, 'Utilisateur/signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Rediriger vers la page de tableau de bord après la connexion

    return render(request, 'Utilisateur/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')
