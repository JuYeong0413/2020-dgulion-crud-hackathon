"""shoppingmall URL Configuration

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
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name="main"), # url에 아무것도 입력하지 않은 경로의 이름(name)은 main, views의 main 함수를 실행한다.
    path('products/', include('products.urls')), # url에 products/가 앞에 붙은 경로는 products의 urls.py를 포함해서 관리한다.
    path('accounts/', include('allauth.urls')), # django-allauth 관련 url을 포함한다.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media 관련 설정
