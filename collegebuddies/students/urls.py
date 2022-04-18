from django.urls import path
from . import views

urlpatterns = [
     # path('', views.index, name='index'),
      path('', views.students, name='students'),
      path('about/', views.about, name='about'),
  #    path('main/', views.main, name='main'),
      path('services/', views.services, name='services')

      ]