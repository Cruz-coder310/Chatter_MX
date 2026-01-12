from django.contrib.auth import views as auth_view
from django.urls import path

from . import views


urlpatterns = [
    path("dashboard/", views.dashboard_panel, name="dashboard"),
    path("accounts/login/", auth_view.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_view.LogoutView.as_view(), name="logout"),
    path("accounts/register/", views.registration, name="registration"),
    # Temporary home page for testing LOGOUT_REDIRECT_URL
    path("", views.home, name="home"),
]
