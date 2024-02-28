from django.contrib.sitemaps import Sitemap
from articles.models import Article, Category, Tag

class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.created