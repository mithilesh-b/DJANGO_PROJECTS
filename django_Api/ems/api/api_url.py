from django.contrib import admin
from django.urls import include, path
from . import views
from rest_framework import routers

rt = routers.DefaultRouter()
#register the viewSet with this router
rt.register(r'companies',views.CompanyViewSet)
rt.register(r'employees',views.EmployeeViewSet)

urlpatterns = [
    # path('sample-data/', views.sample_data, name='sample-data')
    path('',include(rt.urls))
]
