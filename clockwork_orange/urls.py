from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('challenge/<int:pk>/', views.challenge_view, name='challenge'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
