from django.urls import path

from .views import index, video_loader

urlpatterns = [
	path('video/download/', video_loader, name='video_loader'),
	# path('video/', v_download, name='v_download'),
	path('', index, name='home'),
]
