from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse

# from .models import Video

import youtube_dl
# import uuid

from pytube import YouTube
import os


def index(request):
	return render(request, 'main/index.html')


def video_loader(request):
	video_url = request.POST.get('url', '')

	homedir = os.path.expanduser("~")
	dirs = homedir + '/Downloads'

	ydl_opts = {
		# 'format': 'bestvideo',
		'outtmpl': f'{dirs}/%(title)s.%(ext)s'
	}

	if request.method == 'POST':
		youtube_dl.YoutubeDL(ydl_opts).download([video_url])
		return HttpResponse("DONE!!!")
	else:
		return HttpResponse("Error!")





