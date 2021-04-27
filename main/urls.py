from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("v1/", views.v1, name="view 1"),
    path("current_forecast/", views.currentinquiry, name="current forecast"),
    path("prior_forecast/", views.prior_forecast, name="prior forecast"),
    path('currentinquiry/', views.currentinquiry, name = None),
    path("observational_inquiry/", views.observational_inquiry, name="observational inquiry"),
    path("preferences/", views.preferences, name="preferences")
]