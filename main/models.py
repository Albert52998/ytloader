from django.db import models


class Video(models.Model):
	'''Модель загружаемого видео'''
	name = models.CharField(max_length=100, verbose_name='Имя')
	file = models.FileField(verbose_name='Файл')

	class Meta:
		verbose_name = 'Видео'

	def __str__(self):
		return self.name