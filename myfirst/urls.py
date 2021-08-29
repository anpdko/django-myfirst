
from django import urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('aeticles/', include('articles.urls')),
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
]
