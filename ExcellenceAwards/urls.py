"""ExcellenceAwards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from .views import home, error_404, about
from awards.views import ArchiveView, AwardView

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about', about, name='about'),
    path('archive', ArchiveView.as_view(), name='archive'),
    path('<slug>', AwardView.as_view(), name='award'),
    
]

handle404 = error_404

# if the DEBUG is on in settings, then append the urlpatterns as below
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
