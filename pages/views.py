from django.shortcuts import render, redirect, HttpResponse
from .forms import DocumentForm
from .models import Document
from .edit import edit
import sqlite3

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        document_name = request.FILES['document'].name
        if form.is_valid():
            form.save()
            #connection = sqlite3.connect('db.sqlite3')
            #cursor = connection.cursor()
            #query = "SELECT document FROM pages_document WHERE document = 'documents/%s'" % (document_name) 
            #document = cursor.execute(query) 
            edit('media/documents/' + document_name)
            redirect('pages/index.html')
    else:
        form = DocumentForm()
    return render(request, 'pages/index.html', {
        'form': form
    })
