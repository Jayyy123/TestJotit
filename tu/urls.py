from django.urls import path
from . import views

urlpatterns = [
    path('jotters/', views.jotters, name='all-jotters'),
    path('jotter/<str:pk>/', views.jotter, name='single-jotter'),
    path('add-jotter/', views.add_jotter, name='add-jotter'),
    path('edit-jotter/<str:pk>/', views.edit_jotter, name='edit-jotter'),
    path('delete-jotter/<str:pk>/', views.delete_jotter, name='delete-jotter'),
]