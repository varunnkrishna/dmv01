
from django.urls import path, include
from .import views
from django.conf.urls import url

urlpatterns = [
   path('', views.homepage, name='homepage'),
   url ('services/', views.services, name='services'),
   url ('portfolio/', views.portfolio, name='portfolio'),
]
