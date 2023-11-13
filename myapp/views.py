from django.http import HttpResponse, JsonResponse
#Se implemento este modulo HTTP
from .models import Project, Task
from django.shortcuts import get_object_or_404 #En caso de que no exista el objeto nos devuelve el error 404
from django.shortcuts import render, redirect #Permite que las visualizaciones se llamen desde un template en html
from .forms import CreateNewTask, CreateNewProject, ViajeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.
# Esto es una funcion
def index(request):
    #return HttpResponse("Index Page") //Asi imprime solo la palabra Index Page
    title = 'Django Course!!'
    return render(request, 'index.html', {'title': title}) #//Asi iprime el template(Plantilla) index.html

def about(request):
    #return HttpResponse('About this')
    username = 'fazt'
    return render(request, 'about.html', {
        'username': username
    })

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    #return JsonResponse(projects, safe=False)
    return render(request, 'projects/projects.html', {'projects': projects})

#def tasks(request, id):
#def tasksv1(request):
    #task = Task.objects.get(id=id) Esta es igual a la linea task = get_object_or_404(Task, id=id) solo que con el nuevo metodo en caso de error le informaria al usuario sobre el error 404
    #task = get_object_or_404(Task, id=id)
    #return HttpResponse('Tasks: %s' % task.title)
    #task = Task.project.get(id=id)
    #tasks = Task.objects.all()
    #return render(request, 'tasks/task.html', {'tasks' : tasks})

def tasks(request):
    return render(request, 'tasks/tasks.html')

def hello(request, username): 
    print(username)
    return HttpResponse("<h1>Mi nombre es jhon, Hola programacion! %s</h1>" % username)#Nos permite poner lo que se va a mostrar en la pagina

def create_task(request):
    #print(request.GET['title'])#Se obtiene el titulo desde consola con valor que ingresen en el formulario
    #print(request.GET['description'])

    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
        'form': CreateNewTask()
    })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=4)#Este es el codigo que permite que los datos del formulario se guarden en la base de datos
        return redirect('tasks') #El valor tasks seria el name que se creo dentro de urls.py
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
        'form': CreateNewProject()
        })
    else:
        #print(request.POST)
        project = Project.objects.create(name=request.POST["name"], age=20)
        return redirect('projects')
        #print(project)
        #return render(request, 'projects/create_project.html', {
        #'form': CreateNewProject()
        #})

def project_detail(request, id):
    #project = Project.objects.get(id=id)
    #print(project)
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })



def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
             'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
        #register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('signin')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Contraseñas no coinciden'
            })
    
def signout(request):
    logout(request)
    return redirect('signin')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario incorrecto'
                })
        else:
            login(request, user)
            return redirect('principal')
    

def principal(request):
    return render(request, 'principal.html')

def capturar_viaje(request):
    if request.method == 'POST':
        form = ViajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('principal')  # Reemplaza 'pagina_exitosa' con la URL a la que quieres redirigir después de enviar el formulario
    else:
        form = ViajeForm()

    return render(request, 'capturar_viaje.html', {'form': form})