from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task
from django.views import generic
from django.db.models import F
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = "index.html"
    '''context_object_name = "latest_title_list"'''
    def get_queryset(self):
        return Task.objects.all()

class MainView(generic.ListView):
    template_name = "todo_list/main.html"
    '''context_object_name = "latest_title_list"'''
    def get_queryset(self):
        return Task.objects.all()

class DetailView(generic.DetailView):
    model = Task
    template_name = "todo_list/details.html"
    def get_queryset(self):
        return Task.objects.all()

def display_task(request):
    tasks = Task.objects.all()
    #template = loader.get_template('todo_list/display_task.html')
    context = {
        'tasks': tasks,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, "todo_list/all_task.html", context)
    

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        task = request.POST['task']
        deadline = request.POST['deadline']
        priority = request.POST['priority']
        status = request.POST['status']
        
        new_task = Task(
            title_text=title,
            task_text=task,
            status_text=status,
            priority_text=priority,
            deadline_date=deadline
        )
        new_task.save()
        return redirect('todo_list:display_task')
    
    return render(request, 'todo_list/add.html')

def update_task(request, id):
    mytask = get_object_or_404(Task, pk=id)
    if request.method == 'POST':
        mytask.title_text = request.POST['title']
        mytask.task_text = request.POST['task']
        mytask.deadline_date = request.POST['deadline']
        mytask.status_text = request.POST['status']
        mytask.priority_text = request.POST['priority']
        
        mytask.save()
        return redirect('todo_list:display_task')
    
    context = {
        'task': mytask,
    }
    return render(request, 'todo_list/update.html', context)

def delete_task(request,id):
   #mytask= Task.objects.get(id=id)
   mytask=get_object_or_404(Task, pk=id)
   mytask.delete()
   return redirect('todo_list:display_task')