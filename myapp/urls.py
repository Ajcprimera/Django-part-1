from django.urls import path
from . import views #aqui estamos diciendo que desde la ruta actual import el archivo

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hello/<str:username>', views.hello, name='hello'),
    path('tasks/', views.tasks, name='tasks'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:id>', views.project_detail, name='project_detail'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_new_project/', views.create_project, name='create_project')
]
