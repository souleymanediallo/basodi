from django.urls import path
from . import views

urlpatterns = [
    path('add_favorite/<str:product_id>/', views.add_favorite, name='favorite-add'),
    path('my-favorite', views.my_favorite, name="my-favorite"),
    path('delete-favorite/<str:product_id>', views.delete_favorite, name="favorite-delete"),
]
