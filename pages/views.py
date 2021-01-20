from django.shortcuts import render, redirect, HttpResponse
from .forms import DocumentForm
from .models import Document
from .edit import edit
import os, sqlite3

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        document_name = request.FILES['document'].name
        if form.is_valid() and document_name.endswith(".doc") or document_name.endswith(".docx"):
            form.save()
            edit('media/documents/' + document_name)
            document_path = 'media/documents/' + document_name
            FilePointer = open(document_path,"rb")
            response = HttpResponse(FilePointer,content_type='application/msword')
            response['Content-Disposition'] = 'attachment; filename=%s' %document_name
            os.remove(document_path)
            return response
            redirect('pages/index.html')
    else:
        form = DocumentForm()
    return render(request, 'pages/index.html', {
        'form': form
    })
