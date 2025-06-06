from django.urls import path
from . import views

# urls do to_do_list

urlpatterns = [
    path('todo/', views.gravar_tarefa, name='todo'),
]