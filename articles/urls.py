from django.urls import path
from . import views

urlpatterns = [
    path('new', views.ArticleCreateView.as_view(), name="article-create"),
    path('list/', views.ArticleListView.as_view(), name="article-list"),
    path('list/<str:pk>/', views.ArticleDetailView.as_view(), name="article-detail"),
    path('list/<str:pk>/update', views.ArticleUpdateView.as_view(), name="article-update"),
    path('list/<str:pk>/delete', views.ArticleDeleteView.as_view(), name="article-delete"),
    path('list/article-user', views.articles_user, name="article-user"),
    path('category/<str:pk>/<slug:slug>', views.CategoryDetail.as_view(), name="category-detail"),
    path('subcategory/<str:pk>/<slug:slug>', views.SubCategoryDetail.as_view(), name="subcategory-detail"),
    path('search/', views.ArticleSearchView.as_view(), name="article-search"),
]