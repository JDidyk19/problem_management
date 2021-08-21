from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_problems, name='my_problems'),
    path('add-problem/', views.add_problem, name='add_problem'),
    path('<str:slug>/', views.detail_problem, name='detail_problem'),
    path('delete-problem/<int:problem_id>/', views.delete_problem, name='delete_problem'),
    path('delete-solution/<int:solution_id>/', views.delete_solution, name='delete_solution'),
]
