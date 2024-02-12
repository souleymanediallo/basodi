from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput

from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["firstname", "email", "zip_code", "password1", "password2",]
        labels = {
            "firstname": "Prénom",
            "email": "Adresse Email",
            "zip_code": "Code postal",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})




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