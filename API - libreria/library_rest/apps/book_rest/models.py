from django.db import models
from simple_history.models import HistoricalRecords

#modelo de bas de datos de nuestros libros
class Book(models.Model):
	title 				= models.CharField('Titulo',max_length=100, null=False, blank=True)
	author				= models.CharField('Autor',max_length=50, null=False, blank=True)
	date_published 		= models.CharField('Fecha De Publicacion',max_length=20, null=False, blank=True)
	editorial           = models.CharField('Editorial',max_length=50, null=False, blank=True)
	literary_genre      = models.CharField('Genero Literario',max_length=50, null=False, blank=True)
    

# Create your models here.
