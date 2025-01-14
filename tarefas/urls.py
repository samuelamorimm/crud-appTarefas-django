from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
   path('tarefas/', views.tarefas, name='home'),
   path('deletar-tarefa/<int:pk>', views.deletar_tarefa, name='deletar_tarefa')
]