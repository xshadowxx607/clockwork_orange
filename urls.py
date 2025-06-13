
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('challenge/<int:pk>/', views.challenge_view, name='challenge'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', views.profile_view, name='profile'),
    path('register/', views.register, name='register'),
]
