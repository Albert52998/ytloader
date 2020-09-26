# from django.forms import ModelForm, TextInput

# from .models import Video


# class VideoForm(ModelForm):
# 	'''Главная форма'''
# 	class Meta:
# 		model = Video
# 		fields = ['url']
# 		widgets = {'url': TextInput(attrs={
# 			'class': 'header__input',
# 			'id': 'header__input',
# 			'autocomplete': 'off',
# 			'maxlength': '100',
# 			'placeholder': 'Enter link...'
# 		})}