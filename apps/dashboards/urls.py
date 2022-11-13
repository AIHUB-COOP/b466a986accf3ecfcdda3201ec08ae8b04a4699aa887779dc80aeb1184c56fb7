# from .views import render_plots, render_charts
from apps.dashboards import views
from django.urls import path, re_path

urlpatterns = [

    # The home page
    path('plotly', views.render_plots, name='Plotly Graphs'),
    path('chart', views.render_charts, name='Chart JS Graphs'),
    path('maps', views.calculate_distance_view, name='Maps View'),
]