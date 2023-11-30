from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Videos, Guardar_Videos
from .models import UserForm
from .models import VideoForm

# Create your views here.

def videos(request):
    templete = loader.get_template('Usuarios.html')
    context = {
        'usuarios' : Videos.objects.all().values()
    }

    return HttpResponse(templete.render(context, request))

def videos_guardados(request):
    templete = loader.get_template('Guardar_Videos.html')
    context = {
        'videos_guardados' : Guardar_Videos.objects.all().values()
    }

    return HttpResponse(templete.render(context, request))

def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Videos")
    else:
        form = UserForm()
    return render(request, template_name="crear_usuario.html", context={"formuser": form})

def video_register(request):
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("videos_guardados")
    else:
        form = VideoForm()
    return render(request, template_name="registra_videos.html", context={"formvideos": form})