from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('~', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.register, name='register'),
    path('@<str:username>/', views.profile, name='profile'),
    path('logout/', LogoutView.as_view(next_page="/"), name='logout'),
]
