from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm


def home(request):
    return render(request, "home.html")


@login_required()
def dashboard_panel(request):
    return render(request, "accounts/dashboard.html")


def registration(request):
    if request.method == "POST":
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/registration.html", {"form": form})
