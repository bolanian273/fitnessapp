"""CADETS URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

admin.site.site_header = "CADETS ADMIN"
admin.site.index_title = "Dashboard"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fitness_analyser.urls', namespace='fitness_analyser')),
    path('ED/', include('ed_management.urls', namespace='ed_management')),
    path('reports/', include('report.urls', namespace='report')),
    path('authorized/', include('authorized_user.urls', namespace='authorized_user')),
    path('threshold/', include('threshold_managment.urls', namespace='threshold_managment')),
    path('', include('pwa.urls'))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)