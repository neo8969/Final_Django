from django.db import models
from django import forms

# Create your models here.

class Videos(models.Model):
    name = models.CharField(max_length=225)
    nomina = models.CharField(max_length=255)

class Guardar_Videos(models.Model):
    id_del_video = models.IntegerField(null=True)
    video_name = models.CharField(max_length=50)
    extension = models.CharField(max_length=5)
    size = models.IntegerField(null=True)

class Videos_Usuario(models.Model):
    id_usuario = models.IntegerField(null=True)
    id_video = models.IntegerField(null=True)

class UserForm(forms.ModelForm):
    class Meta:
        model = Videos
        fields = ["name", "nomina"]

class VideoForm(forms.ModelForm):
    class Meta:
        model = Guardar_Videos
        fields = ["id_del_video", "video_name", "extension", "size"]