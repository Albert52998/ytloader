# Generated by Django 3.1.1 on 2020-09-24 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media/videos/', verbose_name='Файл'),
        ),
    ]