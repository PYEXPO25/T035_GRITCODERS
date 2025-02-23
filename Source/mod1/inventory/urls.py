from django.urls import path
from . import views  # Correct import

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('schedule/', views.schedule_page, name='schedule'),  # Added '/'
    path('update/<int:schedule_id>/', views.update_completion, name='update_completion'),
]