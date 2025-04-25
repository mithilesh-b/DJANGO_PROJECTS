from . import views
from django.urls import path
urlpatterns = [
    # path('callme/', views.say_hello),
    path('', views.index),
    path('index/', views.index),
    path ('dailyspend/', views.dailyspend, name="dailyspend_URL"),
    
    ]