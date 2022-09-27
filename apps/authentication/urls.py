from django.urls import path
from .views import user_signup_view, login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',login_view, name = 'login' ),
    path('signup/',user_signup_view, name="register"),
    # path("logout/", LogoutView.as_view(), name="logout") for logout after login page
]
