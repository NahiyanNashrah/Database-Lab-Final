"""BloodBankFinal URL Configuration

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
from django.views.generic.base import TemplateView
from BBFApp import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('BBFApp.urls')),
    path('users/', include('django.contrib.auth.urls')),

    # Blood Bank
    path('blood_test_method/', views.blood_test_method, name='blood_test_method'),
    path('show_blood_test/', views.show_blood_test),
    path('store/', views.store),
    path('show_storage/', views.show_storage, name='show_storage'),
    path('storage/', views.storage, name='show_storage'),
    path('create/', views.create, name='create'),
    path('show_donor/', views.show_donor, name='show_donor'),
    path('edit_donor/<int:reg_no>', views.edit_donor, name='edit_donor'),
    path('show_info/', views.show_info, name='show_info'),
    path('receive/', views.receive, name='receive'),
    path('show_recipient/', views.show_recipient, name='show_recipient'),
    path('edit_bag/<int:bag_id>', views.edit_bag),

]
