from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from .views import signup, SecureLoginView, profile

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", SecureLoginView.as_view(), name="login"),

    # Logout must be a POST request in Django 5
    path("logout/", LogoutView.as_view(), name="logout"),

    # Profile
    path("profile/", profile, name="profile"),
    
    # Password Change (uses Django's built-in PasswordChangeView)
    path(
        "password/change/",
        PasswordChangeView.as_view(
            template_name="accounts/password_change.html",
        ),
        name="password_change",
    ),
    path(
        "password/change/done/",
        PasswordChangeDoneView.as_view(
            template_name="accounts/password_change_done.html",
        ),
        name="password_change_done",
    ),
]
