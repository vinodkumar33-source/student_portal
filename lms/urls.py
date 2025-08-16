from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_student, name='add_student'),
    path('search/', views.search_student, name='search_student'),
    path('delete/', views.delete_student, name='delete_student'),
    path('students/', views.view_students, name='view_students'),
]
