from django.urls import path
from core.views import (
    SignUpView,
    HomeView,
    EditUserProfileView,
)
from django.contrib.auth.views import LoginView, LogoutView

app_name = "core"

urlpatterns = [
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("accounts/profile/", EditUserProfileView.as_view(), name="profile"),
    path("home/", HomeView.as_view(), name="home"),
    path("", LoginView.as_view(), name="login"),
]
