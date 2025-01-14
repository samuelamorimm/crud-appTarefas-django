from django.shortcuts import redirect, render, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm
# Create your views here.


def tarefas(request):
    if request.method == 'GET':
        tarefas = Tarefa.objects.all()
        
    
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = TarefaForm()

    
    context = {
        'tarefas' : tarefas,
        'form' : form
    }

    return render(request, 'index.html', context)

def deletar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.delete()
    return redirect('home')