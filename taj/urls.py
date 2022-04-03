from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('jotters/', views.jotters, name='jotters'),
    path('add_jotter/', views.add_jotters, name='add_jotter'),
    path('edit_jotter/<str:pk>/', views.edit_jotters, name='edit_jotter'),
    path('jotter/<str:pk>/', views.jotter, name='jotter'),
]