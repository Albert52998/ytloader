from django.shortcuts import render
from django.http import HttpResponse

import youtube_dl
import os


def index(request):
	return render(request, 'main/index.html')


def video_loader(request):
	video_url = request.POST.get('url', '')

	homedir = os.path.expanduser("~")
	dirs = homedir + '/Downloads'

	ydl_opts = {
		'format': 'best',
		'outtmpl': f'{dirs}/%(title)s.%(ext)s'
	}

	if request.method == 'POST':
		youtube_dl.YoutubeDL(ydl_opts).download([video_url])
		return HttpResponse("""
			<style>html,body{padding:0;margin:0;min-height:100vh;width:100%;background:#121212}a{text-decoration:none;color:#fff}.container{min-width:1050px;max-width:1050px;position:relative;top:0;left:0;right:0;bottom:0;margin:auto}.header{position:relative;top:0;left:0;min-width:100%;height:63px;background-color:#0c1013;border:none;-webkit-box-shadow:0 0 19px 2px rgba(0,0,0,.91);box-shadow:0 0 19px 2px rgba(0,0,0,.91);align-items:center;display:flex;z-index:3;outline:none;user-select:none;color:#fff}.header>.container>div{display:flex;align-items:center}.logo{display:inline;margin: 0 0 -5px 0;font-family:'Noto Sans JP',sans-serif;font-weight:bold;font-size:48px;letter-spacing:.5px}.help{display:inline;margin:0 0 -5px 0;font-family:'Roboto',sans-serif;font-weight:bold;font-size:27px;letter-spacing:.5px;position:absolute;right:0}.sign{min-height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;position:absolute;top:0;left:0;right:0;bottom:0;margin:auto}.sign__word{font-family:'Pacifico',sans-serif;font-size:5.6rem;text-align:center;line-height:1;color:#c6e2ff;animation:neon 0.08s ease-in-out infinite alternate}@keyframes neon{from{text-shadow:0 0 6px rgba(202,228,225,0.92),0 0 30px rgba(202,228,225,0.34),0 0 12px rgba(30,132,242,0.52),0 0 21px rgba(30,132,242,0.92),0 0 34px rgba(30,132,242,0.78),0 0 54px rgba(30,132,242,0.92)}to{text-shadow:0 0 6px rgba(202,228,225,0.98),0 0 30px rgba(202,228,225,0.42),0 0 12px rgba(30,132,242,0.58),0 0 22px rgba(30,132,242,0.84),0 0 38px rgba(30,132,242,0.88),0 0 60px #1e84f2}}</style> <!--<link rel="stylesheet" href="{% static 'css/fonts.css' %}">--> <header class="header"><div class="container"><div><a class="logo" href="/">YTLoader</a><a class="help" href="#0">Help</a></div></div></header><div class="sign"><span class="sign__word">DOWNLOAD COMPLETE!</span></div>
		""")
	else:
		return HttpResponse("""
			<style>html,body{padding:0;margin:0;min-height:100vh;width:100%;background:#121212}a{text-decoration:none;color:#fff}.container{min-width:1050px;max-width:1050px;position:relative;top:0;left:0;right:0;bottom:0;margin:auto}.header{position:relative;top:0;left:0;min-width:100%;height:63px;background-color:#0c1013;border:none;-webkit-box-shadow:0 0 19px 2px rgba(0,0,0,.91);box-shadow:0 0 19px 2px rgba(0,0,0,.91);align-items:center;display:flex;z-index:3;outline:none;user-select:none;color:#fff}.header>.container>div{display:flex;align-items:center}.logo{display:inline;margin: 0 0 -5px 0;font-family:'Noto Sans JP',sans-serif;font-weight:bold;font-size:48px;letter-spacing:.5px}.help{display:inline;margin:0 0 -5px 0;font-family:'Roboto',sans-serif;font-weight:bold;font-size:27px;letter-spacing:.5px;position:absolute;right:0}.sign{min-height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;position:absolute;top:0;left:0;right:0;bottom:0;margin:auto}.sign__word{font-family:'Pacifico',sans-serif;font-size:5.6rem;text-align:center;line-height:1;color:#c6e2ff;animation:neon 0.08s ease-in-out infinite alternate}@keyframes neon{from{text-shadow:0 0 6px rgba(202,228,225,0.92),0 0 30px rgba(202,228,225,0.34),0 0 12px rgba(30,132,242,0.52),0 0 21px rgba(30,132,242,0.92),0 0 34px rgba(30,132,242,0.78),0 0 54px rgba(30,132,242,0.92)}to{text-shadow:0 0 6px rgba(202,228,225,0.98),0 0 30px rgba(202,228,225,0.42),0 0 12px rgba(30,132,242,0.58),0 0 22px rgba(30,132,242,0.84),0 0 38px rgba(30,132,242,0.88),0 0 60px #1e84f2}}</style> <!--<link rel="stylesheet" href="{% static 'css/fonts.css' %}">--> <header class="header"><div class="container"><div><a class="logo" href="/">YTLoader</a><a class="help" href="#0">Help</a></div></div></header><div class="sign"><span class="sign__word">DOWNLOAD COMPLETE!</span></div>
		""")





