# Generated by Django 3.1.1 on 2020-09-19 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='videos/', verbose_name='Файл'),
        ),
    ]
