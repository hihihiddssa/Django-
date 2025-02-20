from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('add_drug/', views.add_drug, name='add_drug'),
    path('edit_drug/<int:drug_id>/', views.edit_drug, name='edit_drug'),
    path('delete_drug/<int:drug_id>/', views.delete_drug, name='delete_drug'),
]