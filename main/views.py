from django.shortcuts import render

from .models import Video


def index(request):
	videos = Video.objects.all()
	return render(request, 'main/index.html')