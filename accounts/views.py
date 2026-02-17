from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from .forms import SignupForm

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})

class SecureLoginView(LoginView):
    template_name = "accounts/login.html"
    
# Note: LogoutView in Django 5 does not support GET requests by default for security.
# We will handle the logout button in the templates.