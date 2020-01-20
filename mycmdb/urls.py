"""mycmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from cmdb.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'assets', AssetViewSet)
router.register(r'ports', PortViewSet)

urlpatterns = [
    path('', BaseView.as_view(), name='baseview'),
    path('addasset/', AddAsset.as_view(), name='addasset'),
    path('addport/', AddPort.as_view(), name='addport'),
    path('edit/<pk>/', UpdateAsset.as_view(), name='updateasset'),
    path('remove/<pk>/', RemoveAsset.as_view(), name='removeasset'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
]
