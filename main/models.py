# from django.db import models
#
#
# class Video(models.Model):
# 	'''Модель загружаемого видео'''
# 	name = models.CharField(max_length=50, verbose_name='Имя')
# 	url = models.CharField(max_length=100, verbose_name='Ссылка')
# 	file = models.FileField(null=True, blank=True, upload_to='videos/', verbose_name='Файл')
#
# 	class Meta:
# 		verbose_name_plural = 'Все видео'
# 		verbose_name = 'Видео'
#
# 	def __str__(self):
# 		return self.name