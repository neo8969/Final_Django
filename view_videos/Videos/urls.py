from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path('videos/', views.videos, name="Videos"),
    path('create_user/', views.create_user, name="crear usuario"),
    path('videos/videos_guardados/', views.videos_guardados, name="videos_guardados"),
    path('video_register/', views.video_register, name="video_register")

]