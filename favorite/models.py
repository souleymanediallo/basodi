from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from articles.models import Article
import uuid

User = get_user_model()


class Favorite(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Article, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return f" {self.username} "
