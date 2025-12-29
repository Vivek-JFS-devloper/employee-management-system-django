"""
URL configuration for emp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.emp_home, name='home'),
    path('add/', views.emp_add, name='add'),
    path('delete/<int:id>/', views.emp_delete, name='delete'),
    path('update/<int:id>/', views.emp_update, name='update'),
    path('contact/' , views.emp_contact,name = 'contact'),
    path('service/' , views.emp_service,name = 'service'),
    path('about/' , views.emp_about,name = 'about'),

]
