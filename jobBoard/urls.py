# job_board_app/urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('user_profile/<str:username>/', user_profile, name='user_profile'),
    path('all_profiles/', all_profiles, name='all_profiles'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    # path('user_profile/<str:username>/', user_profile, name='user_profile'),
    # Add other URLs as needed
]
