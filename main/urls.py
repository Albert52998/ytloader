from django.urls import path

from .views import index, video_loader

urlpatterns = [
	path('video/<int:video_id>/', video_loader, name='video_loader'),
	path('', index, name='home'),
]
