#!/usr/bin/python3
print("Content-type: text/html\n\n")

import cgi
import cgitb; cgitb.enable()
import os

form = cgi.FieldStorage()

fileitem = form['filename']

if fileitem.filename:
    fn = os.path.basename(fileitem.filename)
    open('/tmp/' + fn, 'wb').write(fileitem.file.read())
    print("Файл успешно загружен")
else:
    print("F")
