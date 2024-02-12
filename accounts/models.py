from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import requests

import uuid

class MyUserManager(BaseUserManager):
    def create_user(self, email, firstname, zip_code, password=None):
        if not email:
            raise ValueError('Votre adresse email est obligatoire !')

        user = self.model(email=self.normalize_email(email), firstname=firstname, zip_code=zip_code)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstname, zip_code, password=None):
        user = self.create_user(email, firstname=firstname, zip_code=zip_code, password=password)
        user.is_admin = True
        user.is_staff = True

        user.save(using=self._db)
        return user


def validate_zip_code(value):
    if not value.isdigit() or len(value) != 5:
        raise ValidationError(
            _("%(value)s n'est pas un code postal valide. Un code postal doit contenir exactement 5 chiffres."),
            params={'value': value},
        )

class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    firstname = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=5, validators=[validate_zip_code])
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['firstname', 'zip_code']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(default="user.png", upload_to="photos/%Y/%m", blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    instagram = models.URLField(max_length=400, blank=True, null=True)
    facebook = models.URLField(max_length=400, blank=True, null=True)
    youtube = models.URLField(max_length=400, blank=True, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def get_absolute_url(self):
        return reverse("user-profile", kwargs={"pk": self.pk})


class Address(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    city = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    district = models.CharField(max_length=200, blank=True, null=True)
    department = models.CharField(max_length=200, blank=True, null=True)
    commune = models.CharField(max_length=200, blank=True, null=True)
    region = models.CharField(max_length=200, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.city


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(post_save_receiver, sender=CustomUser)


@receiver(post_save, sender=CustomUser)
def create_or_update_user_address(sender, instance, created, **kwargs):
    if created:
        # Création d'une nouvelle instance d'Address lors de la création de CustomUser
        address = Address(user=instance)
    else:
        # Tentative de récupération de l'adresse existante de l'utilisateur lors de la mise à jour
        address, _ = Address.objects.get_or_create(user=instance)

    # Utilisez le zip_code de CustomUser pour mettre à jour l'adresse
    try:
        response = requests.get(f"https://api-adresse.data.gouv.fr/search/?q=postcode={instance.zip_code}")
        response.raise_for_status()
        data = response.json()

        if data['features']:
            feature = data['features'][0]
            address.city = feature['properties']['city']
            address.longitude = feature['geometry']['coordinates'][0]
            address.latitude = feature['geometry']['coordinates'][1]
            context = feature['properties']['context'].split(',')
            if len(context) >= 3:
                address.department = context[0]
                address.region = context[2]
            address.save()
        else:
            print("Aucune donnée trouvée pour ce code postal.")
    except requests.RequestException as e:
        print(f"Erreur lors de l'appel à l'API : {e}")