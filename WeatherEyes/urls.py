"""WeatherEyes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('register/', v.register, name='register'),
    #path('login/', v.login, name='login'), #Note: This is commented out, because the django app creates it's own login pathway by default. If we include this, it will overwrite the the default django login.
    path('preferences/', include("main.urls"), name='preferences'),
    path('home/', include("main.urls"), name='home'),
    path('current_forecast/', include("main.urls"), name='current forecast'),
    path('observational_inquiry/', include("main.urls"), name='observational inquiry'),
    path('prior_forecast/', include("main.urls"), name='prior_forecast'),
    path('', include("django.contrib.auth.urls")),
]
