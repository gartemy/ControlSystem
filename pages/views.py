from django.shortcuts import render, HttpResponse
from .forms import DocumentForm
from .models import Document

def index(request):
    return render(request, 'pages/index.html')

def upload_form(request):
    return render(request, 'pages/upload.html')

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return 'pages/upload.html'
    return render(request, 'pages/index.html', {
        'form': form
    })
