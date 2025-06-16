from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoList 

# Render 

def crud_tarefa(request):
    tarefa_edicao = None
    
    # POST -> Envio de dados
    # GET  -> Recebimento de dados
    if request.method == 'POST':
        id = request.POST.get("id")
        descricao = request.POST.get("descricao")
        status = bool(request.POST.get("status")) # True ou False
        acao = request.POST.get("acao")  # pode ser None, 'excluir', etc.
        
        if acao == 'excluir':
            tarefa = get_object_or_404(ToDoList, id=id)
            tarefa.delete()

        elif id:  # edição
            tarefa = get_object_or_404(ToDoList, id=id)
            tarefa.descricao = descricao
            tarefa.status = status
            tarefa.save()

        else:  # criação
            nova_tarefa = ToDoList(descricao=descricao, status=status)
            nova_tarefa.save()

        # este redirect é importante para evitar o usuário pressionar F5 e salvar novamente
        return redirect('todo')
        
    # Verifica se veio um ?editar=ID na URL (entrar no modo Edicao)
    if 'editar' in request.GET:
        tarefa_edicao = get_object_or_404(ToDoList, id=request.GET.get('editar'))
    
    
    ###########################################
    # Listar todas tarefas do banco de dados  #
    ###########################################
    
    ## Criar um contador, exemplo: Completas: 1 | Incompletas: 10
    
    tarefas = ToDoList.objects.all()
    # Filtrar todas tarefas, para usar no template
    
    tarefas_completas = ToDoList.objects.filter(status=True).values().count()
    # Conta quantas tarefas estão completas
    
    tarefas_incompletas = ToDoList.objects.filter(status=False).values().count()
    # Conta quantas tarefas estão incompletas
    
    
    # Contexto, será utilizado no 'for' dentro do html
    contexto = {
        'tarefas': tarefas,
        'tarefas_completas': tarefas_completas,
        'tarefas_incompletas': tarefas_incompletas,
        'tarefa_edicao': tarefa_edicao,
    }
    
    return render(request, 'to_do.html', contexto)
