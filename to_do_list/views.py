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
    
    # Este trecho abaixo serve para listar todas tarefas
    
    tarefas = ToDoList.objects.all()
    # Filtrar todas tarefas
    
    # Contexto, será utilizado no 'for' dentro do html
    contexto = {
        'tarefas': tarefas, 
    }
    
    return render(request, 'to_do.html', contexto)
    

def editar_tarefa(request):
    ...
    

def excluir_tarefa(request):
    ...
    

def listar_tarefa(request):
    tarefas = ToDoList.objects.all()
    # Filtrar todas tarefas
    
    # Contexto
    contexto = {
        'tarefas': tarefas, 
    }
    
    return render(request, 'to_do.html', contexto)