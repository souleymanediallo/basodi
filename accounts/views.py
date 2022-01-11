from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, ProfileUpdateForm, UserUpdateForm
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


@login_required
def dashboard(request):
    return render(request, "accounts/dashboard.html")


# Update Profile user
@login_required
def profile_update(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get("username")
            messages.success(
                request,
                f"Votre compte a été mis à jour {username}")
            return redirect('dashboard')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {"u_form": u_form, "p_form": p_form}
    return render(request, "accounts/update.html", context)