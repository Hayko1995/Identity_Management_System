"""social_djoser URL Configuration

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
from social_djoser.token import CustomJWTToken
from social_djoser.oauth.google import ObtainUserFromGoogle

from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from accounts.models import User
from social_djoser.views import UserChangePasswordView, CutomObtainPairView, ResetPasswordView
from rest_framework_simplejwt.views import TokenBlacklistView
from two_factor.urls import urlpatterns as tf_urls
from accounts.admin import admin_site


urlpatterns = [
    # Original Admin panel
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('blog/', include('blog.urls')),

    # URLs for Djoser/Django social OAuth2 login.
    path('api/auth/social/', include('djoser.social.urls')),
    path('api/auth/social_django/',
         include('social_django.urls', namespace='social')),
    path('accounts/profile/', ObtainUserFromGoogle.as_view()),
    path('api/auth/', include('djoser.urls.jwt')),

    path('api/auth/jwt/create', CustomJWTToken.as_view(), name='login'),
    path('updateUser/', UserChangePasswordView.as_view(), name='updateUser'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
    path('auth/jwt/create/', CutomObtainPairView.as_view(), name='login'),
    path('resetPassword/', ResetPasswordView.as_view(), name='customtoken'),

    path('otp/', admin_site.urls),
]
