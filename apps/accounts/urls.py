from django.contrib.auth import views as auth_view
from django.urls import path

from . import views


urlpatterns = [
    path("dashboard/", views.dashboard_panel, name="dashboard"),
    path("accounts/login/", auth_view.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_view.LogoutView.as_view(), name="logout"),
    path("accounts/register/", views.registration, name="registration"),
    path(
        "accounts/password-change/",
        auth_view.PasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "accounts/password-change/done/",
        auth_view.PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    # Temporary home page for testing LOGOUT_REDIRECT_URL
    path("", views.home, name="home"),
]
