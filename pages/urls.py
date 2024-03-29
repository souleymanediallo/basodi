from django.urls import path
from . import views
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ArticleSitemap

sitemaps = {
    "articles": ArticleSitemap,
}

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('utilisation', views.UtilisationView.as_view(), name="utilisation"),
    path('mentions-legales', views.MentionsLegalsView.as_view(), name="mentions"),
    path('conditons-generales-d-utilisation', views.CguView.as_view(), name="cgu"),
    path('nos-valeurs', views.ValuesView.as_view(), name="valeurs"),
    path('qui-sommes-nous', views.SocieteView.as_view(), name="societe"),
    path('nos-conseils', views.ConseilView.as_view(), name="conseils"),
    path('nos-engagements', views.EngagementView.as_view(), name="engagements"),
    path('foire-aux-question', views.FaqView.as_view(), name="faq"),
    path("robots.txt", views.robots_txt),

    # sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

]
