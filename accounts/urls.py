from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import signup, SecureLoginView

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", SecureLoginView.as_view(), name="login"),
    # Logout must be a POST request in Django 5
    path("logout/", LogoutView.as_view(), name="logout"),
]