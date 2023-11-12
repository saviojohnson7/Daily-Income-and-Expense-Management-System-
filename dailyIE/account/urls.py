"""
URL configuration for dailyIE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.home1),
    path('reg',v.reg1),
    # path('reg12',v.addincome,name='reg12'),
    path('login_link',v.login12),
    # path('otp',v.otp_view,name='otp'),
    path('logout1',v.logout12),
    path('edit_profile',v.edit1),
    path('cngu',v.change_name),
    path('about',v.about1),
    
   

]
