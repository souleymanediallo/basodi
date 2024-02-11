from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput

from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["user_choices", "firstname", "email", "password1", "password2", "city"]
        labels = {
            "user_choices": "Type de compte",
            "firstname": "Prénom",
            "email": "Adresse Email",
            "city": "Votre Ville",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['user_choices'].widget.attrs.update({'class': 'form-control custom-select'})
        self.fields['city'].widget = TextInput(attrs={
            'id': 'auto_check',
            'class': 'form-control',
            'placeholder': 'Ville'
        })


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ["firstname"]
        labels = {
            "firstname": "Prénom",
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['last_name', 'image', 'phone', 'instagram', 'facebook', 'youtube', 'description']
        labels = {
            "last_name": "Nom",
            "phone": "Téléphone",
            "location": "Région",
            "instagram": "Lien instagram",
            "facebook": "Lien facebook",
            "youtube": "Lien youtube",
            "description": "Quelques mots pour votre présenter à la communauté",
        }