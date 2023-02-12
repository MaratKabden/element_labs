"""shopback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.urls import include
from api.views import ProductList, ProductDetail, CategoryList, CategoryDetail, CategoryProductList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/products/', ProductList.as_view()),
    path('api/products/<int:pk>/', ProductDetail.as_view()),
    path('api/categories/', CategoryList.as_view()),
    path('api/categories/<int:pk>/', CategoryDetail.as_view()),
    path('api/categories/<int:id>/products/', CategoryProductList.as_view()),
]
