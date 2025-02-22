from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('create/', views.note_create, name='note_create'),
    path('delete/<int:pk>/', views.note_delete, name='note_delete'),
    path('complete/<int:pk>/', views.mark_completed, name='mark_completed'),  # Add this line
]