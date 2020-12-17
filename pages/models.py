from __future__ import unicode_literals
from django.db import models


class Document(models.Model):
    document = models.FileField(upload_to='', verbose_name="Документ")

    def __str__(self):            
        return self.document.name

    class Meta:
        verbose_name = 'документ'
        verbose_name_plural = 'Документы'
