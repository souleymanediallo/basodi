from django.urls import path
from . import views

urlpatterns = [
    path('new', views.ArticleCreateView.as_view(), name="article-create"),
    path('list/', views.ArticleListView.as_view(), name="article-list"),
    path('list/<str:pk>/', views.ArticleDetailView.as_view(), name="article-detail"),
    path('list/<str:pk>/update', views.ArticleUpdateView.as_view(), name="article-update"),
    path('list/<str:pk>/delete', views.ArticleDeleteView.as_view(), name="article-delete"),
    path('list/article-user', views.articles_user, name="article-user"),
    path('category/<slug:slug>', views.CategoryDetail.as_view(), name="category-detail"),
    path('subcategory/<slug:slug>', views.SubCategoryDetail.as_view(), name="subcategory-detail"),
    path('search/', views.ArticleSearchView.as_view(), name="article-search"),
    path('api/get-categories-for-gender/<str:gender_name>/', views.get_categories_for_gender,
         name='get_categories_for_gender'),
    path('api/get-subcategories-for-category/<str:category_id>/', views.get_subcategories_for_category,
         name='get_subcategories_for_category'),
    # path('get-subcategories-for-gender/', views.get_subcategories_for_gender, name='get-subcategories-for-gender'),
]