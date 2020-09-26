from django.shortcuts import render, redirect

from .models import Video

import youtube_dl
import uuid


def index(request):
	last_video = Video.objects.last()
	current_video = Video.objects.get(pk=last_video.pk)
	return render(request, 'main/index.html', {'current_video': current_video})


def video_loader(request, video_id):
	video_url = request.GET.get('url', '')

	filename = str(uuid.uuid4())

	ydl_opts = {
		'format': 'bestvideo',
		'outtmpl': f'media/videos/{filename}.%(ext)s'
	}

	if video_url:
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([video_url])
			Video.objects.create(name=filename, url=video_url, file=f'videos/{filename}.mp4')
			# last_video = Video.objects.last()
	else:
		pass

	current_video = Video.objects.get(pk=video_id)

	return redirect(current_video.file.url)




# def by_video(request, video_id):
# 	current_video = Video.objects.get(pk=video_id)
#
# 	video_url = request.GET.get('url', '')
#
# 	filename = str(uuid.uuid4())
#
# 	ydl_opts = {
#         # 'format': 'bestvideo',
#         'outtmpl': f'media/videos/{filename}/{filename}.%(ext)s'
#     }
#
# 	if video_url:
# 		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
# 			ydl.download([video_url])
# 			Video.objects.create(name=filename, url=video_url)
# 			# return redirect('/')
# 	else:
# 		pass
#
# 	return render(request, 'main/by_video.html', {'current_video': current_video})

