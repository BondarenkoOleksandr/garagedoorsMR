"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('articles/', include('articles.urls')),
    # path('accounts/', include('accounts.urls')),
]

urlpatterns += [
    path('api/', include('articles.api.urls')),
    path('api/', include('employees.api.urls')),
    path('api/', include('cities.api.urls')),
    path('api/', include('states.api.urls')),
    path('api/', include('services.api.urls')),
    path('api/', include('reviews.api.urls')),
    path('api/', include('faq.api.urls')),
    path('api/', include('coupons.api.urls')),
    path('api/', include('accounts.api.urls')),
]

urlpatterns += \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
