from django.shortcuts import render

def home(request):
    return render(request, 'book.html')

def test(request):
    return render(request, 'index.html')