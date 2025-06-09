from django.contrib import admin
from to_do_list.models import ToDoList

class TodoListAdmin(admin.ModelAdmin):
    ...
    # list_display
    # search_display
    # Nesta classe eu informo o que será apresentando e o que posso filtrar na url: /admin
    
    """
    O arquivo admin.py serve para registrar seus modelos no painel administrativo do Django (o Django Admin), que é uma interface automática e super útil para criar, visualizar, editar e excluir dados dos modelos do seu projeto — sem precisar escrever código para isso.
    
    """


admin.site.register(ToDoList)
