from typing import Text
from django.shortcuts import render,redirect
from .models import ToDo

def home(request):
    todo_list=ToDo.objects.all()
    return render(request, 'book.html', {"todo_list": todo_list})

def test(request):
    
    return render(request, 'index.html')
