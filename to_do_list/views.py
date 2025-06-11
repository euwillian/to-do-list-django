from django.shortcuts import render, redirect
from .models import ToDoList 

# Render 

def gravar_e_listar_tarefa(request):
    # POST -> Envio de dados
    # GET  -> Recebimento de dados
    
    if request.method == 'POST':
        descricao = request.POST.get("descricao")
        
        # cria uma nova instancia do modelo "ToDoList - Model" , e salva no banco de dados
        
        nova_tarefa = ToDoList(descricao=descricao)
        nova_tarefa.save()
        
        # este redirect é importante para evitar o usuário pressionar F5 e salve novamente
        return redirect('todo')
    
    ###########################################
    # Listar todas tarefas do banco de dados  #
    ###########################################
    
    ## Criar um contador, exemplo: Completas: 1 | Incompletas: 10
    
    tarefas = ToDoList.objects.all()
    # Filtrar todas tarefas
    
    tarefas_completas = ToDoList.objects.filter(status=True).values().count()
    # Conta quantas tarefas estão completas
    
    tarefas_incompletas = ToDoList.objects.filter(status=False).values().count()
    # Conta quantas tarefas estão incompletas
    
    
    # Contexto, será utilizado no 'for' dentro do html
    contexto = {
        'tarefas': tarefas,
        'tarefas_completas': tarefas_completas,
        'tarefas_incompletas': tarefas_incompletas,
    }
    
    return render(request, 'to_do.html', contexto)
    

def editar_tarefa(request):
    ...
    

def excluir_tarefa(request):
    ...
    
