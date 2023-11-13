from django.urls import path
from . import views

urlpatterns = [
    path ('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path ('index/', views.index, name="index"),
    path ('about/', views.about, name="about"),
    path ('hello/<str:username>', views.hello, name="hello"),
    path ('projects/', views.projects, name="projects"),
    path ('projects/<int:id>', views.project_detail, name="project_detail"),
    #path ('tasksv1/', views.tasksv1, name="task")
    path ('tasks/', views.tasks, name="tasks"),
    path ('create_task/', views.create_task, name="crete_task"),
    path ('create_project/', views.create_project, name="create_project"),
    path ('logout/', views.signout, name='logout'),
    path ('signin/', views.signin, name='signin'),
    path ('principal/',views.principal, name="principal"),
    path ('signup/', views.signup, name="registrarse"),
    path('capturar_viaje/', views.capturar_viaje, name='capturar_viaje')
]
