"""Application URL Configuration

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
from Traveler import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home,name="home"),
    path("login",views.Login,name="Login"),
    path("profile",views.profile_info,name="Profile"),
    path("signup",views.Signup,name="signup"),
    path("logout",views.Logout,name="logout"),
    path("book-now/<name>",views.book_now,name="book now"),
    path("search-book-now",views.book_now,name="Search book now"),
    
     
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
