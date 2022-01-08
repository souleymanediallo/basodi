from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm
from django.contrib import messages
from .models import CustomUser, Profile
from articles.models import Article


# Create your views here.
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.firstname = user.firstname.upper()
            user.save()
            messages.success(request, "Votre compte a été crée !")
            return redirect("home")
    else:
        messages.warning(request, 'Tous les champs sont obligatoires !')
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, "accounts/register.html", context)


# https://docs.djangoproject.com/fr/3.2/topics/auth/default/
def login_user(request):
    if request.method == "POST":
        email = request.POST["email"].lower()
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Erreur email ou mot de passe")

    return render(request, "accounts/login.html")


def user_profile(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)

    articles = Article.objects.filter(author=profile.user)

    context = {"profile": profile, "articles": articles}

    return render(request, "accounts/user_profile.html", context)


def dashboard(request):
    return render(request, "accounts/dashboard.html")