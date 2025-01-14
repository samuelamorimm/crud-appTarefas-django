from django.db import models

# Create your models here.
class Tarefa(models.Model):
    title = models.CharField(default='', max_length=255, verbose_name='Título:')
    completed = models.BooleanField(default=False, verbose_name='Completada:')