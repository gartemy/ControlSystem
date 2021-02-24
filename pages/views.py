from django.shortcuts import render, redirect, HttpResponse
from .forms import DocumentForm
from .models import Document
from .edit import edit
import pymysql, os

def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        document_name = request.FILES['document'].name
        if form.is_valid() and document_name.endswith(".doc") or document_name.endswith(".docx"):
            form.save()
<<<<<<< HEAD
            connection = pymysql.connect('localhost', 'root', '', 'controlsystem')
            cursor = connection.cursor()
            document= cursor.execute("SELECT document FROM pages_document WHERE document = '%s'" %document_name)
            edit('media/' + document )
=======
            connection = sqlite3.connect('db.sqlite3')
            cursor = conn.cursor()
            document = execute("SELECT document FROM pages_document WHERE document = '%s'" %document_name) 
            edit('media/documents/' + document)
>>>>>>> 5015bb0ca394767e75cd467e12c4907103567b9d
            document_path = 'media/documents/' + document
            FilePointer = open(document_path,"rb")
            response = HttpResponse(FilePointer,content_type='application/msword')
            response['Content-Disposition'] = 'attachment; filename=%s' %document
            os.remove(document_path)
            return response
            redirect('pages/index.html')
    else:
        form = DocumentForm()
    return render(request, 'pages/index.html', {
        'form': form
    })
