from django.urls import path
from .views import user_signup_view, login_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',login_view, name = 'login' ),
    path('signup/',user_signup_view, name="register"),
<<<<<<< HEAD
<<<<<<< HEAD
    path("logout/", LogoutView.as_view(), name="logout") # for logout after login page
=======
    # path("logout/", LogoutView.as_view(), name="logout") for logout after login page
>>>>>>> 1599dc7 (TEM-7 added urls and views for login page(Dummy))
=======
    # path("logout/", LogoutView.as_view(), name="logout") for logout after login page
>>>>>>> f03ce49e300078d90a99e58ab62b1f9da33cffe0
]
