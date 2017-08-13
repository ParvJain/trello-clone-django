from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from kanban.serializers import CategorySerializer
from kanban.models import Category

from rest_framework.decorators import api_view

from rest_framework.response import Response


@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")

def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("User created successfully!")
    else:
        form = UserCreationForm()
        return render(request, 'auth/create_user.html', {'form': form})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@api_view(['GET'])
def category_collection(request):
    if request.method == 'GET':
        posts = Category.objects.all().filter(user__username=request.user)
        serializer = CategorySerializer(posts, many=True)
        return Response(serializer.data)
