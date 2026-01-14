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
    path(
        "accounts/password-reset/",
        auth_view.PasswordResetView.as_view(),
        name="password_reset",
    ),
    path(
        "accounts/password-reset/done/",
        auth_view.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "accounts/reset/<uidb64>/<token>/",
        auth_view.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "accounts/reset/complete/",
        auth_view.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    # Temporary home page for testing LOGOUT_REDIRECT_URL
    path("", views.home, name="home"),
]
