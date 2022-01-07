from django.shortcuts import render
from django.views.generic import ListView
from articles.models import Article


# Create your views here.
class HomeView(ListView):
    model = Article
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.all()
        return context