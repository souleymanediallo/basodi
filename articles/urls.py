from django.urls import path
from . import views

urlpatterns = [
    path('new', views.ArticleCreateView.as_view(), name="article-create"),
]