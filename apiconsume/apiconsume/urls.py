"""
URL configuration for apiconsume project.

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
from . import views
from .views import updatedata

urlpatterns = [
    path('admin/', admin.site.urls),
    path('getdata/', views.get_api_data, name ="get-data"),
    path('form/', views.api_form, name="form"),
    # path('edit/<int:comp_id>/', views.updatedata, name="update"),
    path('delete/<int:comp_id>/', views.deletedata, name="delete"),
    path('edit_data/<int:comp_id>/', views.updatedata, name='edit_data'),
    path('success/', views.success_page, name='success_page'),
]
