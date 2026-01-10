from django.contrib.auth import views as auth_view
from django.urls import path

from . import views


urlpatterns = [
    path("dashboard/", views.dashboard_panel, name="dashboard"),
    path("accounts/login/", auth_view.LoginView.as_view(), name="login"),
]
