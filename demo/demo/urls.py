"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from home import views as home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home.get_home),
    path('them-phong/',home.get_phong),
    path('them-csvc/',home.get_csvc),
    path('addPhong',home.add_phong),
    path('addCsvc',home.add_csvc),
    path('deletePhong/<int:id>/',home.delete_phong),#Xóa
    path('deleteCsvc/<int:id>/',home.delete_csvc),#Xóa
    path('phong/<int:id>/',home.view_phong),#View Sửa
    path('editPhong',home.edit_phong),#Sửa
    path('csvc/<int:id>/',home.view_csvc),# ViewSửa
    path('editCsvc',home.edit_csvc),#Sửa
    path('404',home.get_404),
    path('tao-phong/',home.get_taophong),
    path('createPhong',home.create_phong),
    path('delPh/<int:id>/',home.del_ph),
    path('tao-csvc/',home.get_taocsvc),
    path('createCSVC',home.create_csvc),
    path('delVC/<int:id>/',home.del_vc),
    path('sua-ten-csvc/<int:id>/',home.get_suacsvc),
    path('sua_tenCsvc',home.edit_taocsvc),
    path('sua-ten-Phong/<int:id>/',home.get_suaPhong),
    path('sua_tenPhong',home.edit_taophong),
]
