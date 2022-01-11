from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("profile/<uuid:profile_id>/", views.user_profile, name="user-profile"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('update/', views.profile_update, name="profile-update"),
]