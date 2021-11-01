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


from app.views import index, SitemapView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="GarageDoors API",
      default_version='v1',
      description="API for Garage Doors MR",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="backend@artads.agency"),
      license=openapi.License(name="Garage Doors License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('login/', include('accounts.urls')),
]

urlpatterns += [
    path('api/sitemap', SitemapView.as_view()),
    path('api/', include('articles.api.urls')),
    path('api/', include('employees.api.urls')),
    path('api/', include('cities.api.urls')),
    path('api/', include('states.api.urls')),
    path('api/', include('services.api.urls')),
    path('api/', include('reviews.api.urls')),
    path('api/', include('faq.api.urls')),
    path('api/', include('coupons.api.urls')),
    path('api/', include('accounts.api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
