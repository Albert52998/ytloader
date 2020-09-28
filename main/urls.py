from django.urls import path

from .views import index, video_loader

urlpatterns = [
	path('video/download/', video_loader, name='video_loader'),
	path('', index, name='home'),
]
