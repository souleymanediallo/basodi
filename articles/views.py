from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator

from .models import Article, Category, SubCategory
from .forms import ArticleForm


# Create your views here.
class ArticleListView(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "articles/article_list.html"
    paginate_by = 4


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "articles/article_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['article_similar'] = Article.objects.all()
        return context

   
class ArticleCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Article
    form_class = ArticleForm
    context_object_name = "form"
    success_url = reverse_lazy("home")
    success_message = "Votre article a été crée !"
    template_name = "articles/article_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    context_object_name = "form"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = "articles/article_confirm_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        article = self.get_object()
        if self.request.user == article.author:
            return True
        return False


class CategoryDetail(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "categories/category_detail.html"

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Article.objects.filter(category=self.category)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        context['categories'] = Category.objects.all()
        context['category'] = self.category
        return context


class SubCategoryDetail(ListView):
    model = Article
    context_object_name = "articles"
    template_name = "categories/subcategory_detail.html"

    def get_queryset(self):
        self.subcategory = get_object_or_404(SubCategory, slug=self.kwargs['slug'])
        return Article.objects.filter(subcategory=self.subcategory)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        self.subcategory = get_object_or_404(SubCategory, slug=self.kwargs['slug'])
        context['subcategories'] = SubCategory.objects.all()
        context['subcategory'] = self.subcategory
        return context


class ArticleSearchView(ListView):
    model = Article
    template_name = "articles/search.html"
    context_object_name = "articles"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Article.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(tag__name__icontains=query)
            )
        return Article.objects.all()


@login_required
def articles_user(request):
    articles = Article.objects.filter(author=request.user)
    context = {"articles": articles}
    return render(request, "articles/article_user.html", context)


