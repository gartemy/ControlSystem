import os
from django.conf import settings
from django.db import models

class Document(models.Model):
    document = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.document.name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'