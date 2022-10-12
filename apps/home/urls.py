from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    re_path(r'^.*\.*', views.pages, name='pages'),
]