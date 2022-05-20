"""API_prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from DatosSensores.views import HomeView
from django.views.generic import TemplateView
from DatosSensores import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="../templates/sign_in.html"),name='sign_in'),
    path('home/',HomeView, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('logout_user', views.LogOutUser, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root_=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root_=settings.MEDIA_ROOT)
