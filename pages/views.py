import MySQLdb, os, zipfile
from django.shortcuts import render, HttpResponse
from .models import Document
from .word import word_change
from .edit import edit

def index(request):
    try:
        if request.method == 'POST':
            documents = request.FILES.getlist("document")
            for doc in documents:
                if doc.name.endswith(".docx"):
                    doc.name = word_change(doc.name)
                    Document(document = doc).save()
                else:
                    return render(request, 'pages/index.html')

            for doc in documents:
                edit('ControlSystem/pages/media/documents/' + doc.name)

            connection = MySQLdb.connect('gartemy.mysql.pythonanywhere-services.com', 'gartemy', 'ISiT293901', 'gartemy$controlsystem')
            cursor = connection.cursor()
            for doc in documents:
                if len(documents) == 1:
                    cursor.execute("SELECT document FROM pages_document WHERE document = 'documents/%s'" %doc.name)
                    document = cursor.fetchone()
                    document = document[0]
                    document_path = 'ControlSystem/pages/media/' + document
                    FilePointer = open(document_path,"rb")
                    response = HttpResponse(FilePointer,content_type='application/msword')
                    response['Content-Disposition'] = 'attachment; filename=%s' %doc.name
                    cursor.execute("TRUNCATE TABLE pages_document")
                    os.remove(document_path)
                    return response
                else:
                    os.chdir('ControlSystem/pages/media/documents/')
                    zip_file = zipfile.ZipFile('documents.zip', 'w')
                    for doc in documents:
                        zip_file.write(doc.name)
                        os.remove(doc.name)
                    zip_file.close()
                    FilePointer = open('documents.zip',"rb")
                    response = HttpResponse(FilePointer,content_type='application/octet-stream')
                    response['Content-Disposition'] = 'attachment; filename=documents.zip'
                    cursor.execute("TRUNCATE TABLE pages_document")
                    os.remove('documents.zip')
                    return response
        return render(request, 'pages/index.html')
    except:
        return render(request, 'pages/error.html')
