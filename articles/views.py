from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Article
from .forms import ArticleForm


# Create your views here.
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    context_object_name = "form"
    success_url = reverse_lazy("home")
    success_message = "Votre annonce a été crée !"
    template_name = "articles/article_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)