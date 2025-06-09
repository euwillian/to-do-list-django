from django.db import models


class ToDoList(models.Model):
    descricao = models.CharField(max_length=100, null=False, blank=False)
    status = models.BooleanField(default=False, null=False, blank=False)
    
    # Classe que irá gravar a descricao da tarefa e o status (True ou False) > Completo/Nao completo
    
    def __str__(self):
        return self.descricao
