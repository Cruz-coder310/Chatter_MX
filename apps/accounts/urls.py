from django.urls import path, include

from . import views


urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("dashboard/", views.dashboard_panel, name="dashboard"),
    path("accounts/register/", views.registration, name="registration"),
    path("accounts/edit_profile/", views.edit_profile, name="edit_profile"),
    # Temporary home page for testing LOGOUT_REDIRECT_URL
    path("", views.home, name="home"),
]
