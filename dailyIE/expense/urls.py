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
    path('addexpense',v.addexpense1),
    path('expenselist',v.data2,name='list'),
    path('deleteE/<int:id>',v.delete_E),
    path('editE/<int:id>',v.edit_E),
    path('expense_search',v.expense_search2,name='expense_search'),
    path('extp/<str:ext>',v.sort_data,name='ext'),
    path('pay',v.payment1),

]
