from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, UserEditForm


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


@login_required()
def edit_profile(request):
    if request.method == "POST":
        form = UserEditForm(
            data=request.POST,
            files=request.FILES,
            instance=request.user,
        )
        if form.is_valid():
            form.save()
    else:
        form = UserEditForm(instance=request.user)

    return render(request, "accounts/edit_profile.html", {"form": form})
