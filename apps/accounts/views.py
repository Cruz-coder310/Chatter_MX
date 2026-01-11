from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")


@login_required()
def dashboard_panel(request):
    return render(request, "accounts/dashboard.html")
