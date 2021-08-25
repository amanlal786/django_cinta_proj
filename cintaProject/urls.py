"""cintaProject URL Configuration

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
from usersProfile import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('userinfo/', views.user_list),
    path('userinfo/<int:pk>', views.user_detail),
    path('',views.home),
    path('user',views.home2, name='user'),
    path('login', auth_views.LoginView.as_view(template_name='usersProfile/home2.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='usersProfile/logout.html'), name='logout'),
    path('edit/<int:pk>/', views.edit, name='edit'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
