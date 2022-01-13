from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from articles.models import Article


# Create your views here.
class HomeView(ListView):
    model = Article
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["articles"] = Article.objects.all()
        return context


class UtilisationView(TemplateView):
    template_name = "pages/utilisation.html"


class SocieteView(TemplateView):
    template_name = "pages/qui-sommes-nous.html"


class MentionsLegalsView(TemplateView):
    template_name = "pages/mentions-legales.html"


class ConseilView(TemplateView):
    template_name = "pages/conseils.html"


class EngagementView(TemplateView):
    template_name = "pages/engagements.html"


class ValuesView(TemplateView):
    template_name = "pages/valeurs.html"


class CguView(TemplateView):
    template_name = "pages/conditions-generales-d-utilisation.html"


class FaqView(TemplateView):
    template_name = "pages/foire-aux-questions.html"