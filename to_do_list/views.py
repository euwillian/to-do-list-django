from django.shortcuts import render

# Render 

def gravar_tarefa(request):
    contexto = {
        'mostrar_print': "Print de contexto",
        }
    
    return render(request, 'to_do.html', contexto)
    
    
    # if request.method == 'POST':
    #    form = ToDoForm(request.POST, instance=tarefa)
    #    if form.is_valid():
    #        form.save()
    #    else:
    #        form = ToDoForm(instance=tarefa)
    

def editar_tarefa(request):
    ...
    

def excluir_tarefa(request):
    ...
    

def listar_tarefa(request):
    ...