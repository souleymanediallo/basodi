from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from django.urls import reverse

from .choices import CITY_CHOICES

import uuid


class MyUserManager(BaseUserManager):
    def create_user(self, email, firstname, city, user_choices, password=None):
        if not email:
            raise ValueError('Votre adresse email est obligatoire !')

        user = self.model(email=self.normalize_email(email), firstname=firstname, city=city, user_choices=user_choices)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, firstname, city, user_choices, password=None):
        user = self.create_user(email, firstname=firstname, city=city, user_choices=user_choices, password=password)
        user.is_admin = True
        user.is_staff = True

        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):

    USER_CHOICES = (
        ('PARTICULIER', 'PARTICULIER'),
        ('PROFESSIONNEL', 'PROFESSIONNEL')
    )
    email = models.EmailField(max_length=255, unique=True)
    firstname = models.CharField(max_length=200)
    user_choices = models.CharField(max_length=50, choices=USER_CHOICES, default='PARTICULIER')
    city = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['firstname', 'user_choices', 'city']

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


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(post_save_receiver, sender=CustomUser)