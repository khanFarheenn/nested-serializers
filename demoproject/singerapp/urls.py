from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world),
    path('singers/', views.get_singer, name='singer-list'),
    path('singers/<int:pk>/', views.get_singer,name='singer-list'),
    path('songs/', views.get_songs, name='song-list'),
    path('songs/<int:pk>/', views.get_songs),
]
