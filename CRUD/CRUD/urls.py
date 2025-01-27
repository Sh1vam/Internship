"""
URL configuration for CRUD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from phone_book.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('display_contacts/', display_contacts, name='display_contacts'),
    path('display_contacts/details/<int:id>', details, name='details'),
    path('add_contact/', add_contact, name='add_contact'),
    path('display_contacts/details/update_contact/<int:id>', update_contact, name='update_contact'),
    path('display_contacts/details/delete_contact/<int:id>', delete_contact, name='delete_contact'),
]
