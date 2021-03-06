from django.shortcuts import render,redirect
from .models import Personagem,Habs,User2
from django.http import HttpResponse
from django.contrib.auth import logout
from .forms import CharacterForm,LogUser,CreateHabForm
from hashlib import md5
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
def index(request):
    data = Personagem.objects.all()
    return render(request,'app/index.html',{'data':data})
def character(request,id):
    data = Personagem.objects.filter(id = id)
    data2 = Habs.objects.filter(fk_id = id)
    return render(request,'app/character.html',{'habs':data2,'person':data})
def character_creator(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CharacterForm()
    return render(request,'app/characterCreate.html',{'form':form})
def Login(request):
    if request.method == 'POST':
        form = LogUser(request.POST)
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request,username=name, password=password)
        if user is not None:
            login(request,user)
            print('nhe')
            redirect('/')
        else:
            redirect('/nhe')
    else:
        form = LogUser()
    return render(request, 'app/Login.html', {'form': form})
def CreateHab(request):
    if request.method == 'POST':
        form = CreateHabForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateHabForm()
    return render(request,'app/CreateHab.html',{'form':form})
def updateCharacter(request,id):
    post = get_object_or_404(Personagem,id=id)
    if request.method == 'POST':
        form = CharacterForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CharacterForm()
    return render(request, 'app/CreateHab.html', {'form': form})