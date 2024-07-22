from django.contrib.auth import login, authenticate, logout, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
User = get_user_model()
def signup(request):
    if request.method == "POST":
        # Récupérer les informations de l'utilisateur
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Créer un nouvel utilisateur
        user = User.objects.create_user(username=username, password=password)
        login(request, user)  # Connecter l'utilisateur
        return redirect('index')  # Rediriger vers la page d'accueil

    return render(request, 'accounts/signup.html')


def login_user(request):
    if request.method == "POST":
        # connecter l'utilisateur
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, 'accounts/login.html')



def logout_user(request):
    logout(request)
    return redirect('index')