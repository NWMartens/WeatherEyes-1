from django.urls import path

from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("v1/", views.v1, name="view 1"),
    path("current_forecast/", views.current_forecast, name="current forecast"),
    path("prior_forecast/", views.prior_forecast, name="prior forecast"),
    path("observational_inquiry/", views.observational_inquiry, name="observational inquiry"),
    path("preferences/", views.preferences, name="preferences"),
    path('image/',views.image, name = 'image')
]