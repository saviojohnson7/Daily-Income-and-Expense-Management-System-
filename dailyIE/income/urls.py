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
    path('inc',v.addincome2),
    path('incomelist',v.data1,name='ilist'),
    path('delete1/<int:id>',v.delete_emp),
    path('edit/<int:id>',v.edit1),
    path('income_search',v.income_search2,name='income_search'),
    path('ixtp/<str:ixt>',v.sort_data1,name='ixt'),
]
