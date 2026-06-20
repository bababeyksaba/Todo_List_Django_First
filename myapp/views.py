from django.shortcuts import render,redirect
from .models import Task

def task_list(request):
    if request.method == "POST":
        title=request.POST.get("title")
        Task.objects.create(title=title)
    
        return redirect("/")

    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})

def complete_task():
    task =Task.objects.get(id=pk)
    task.complete=True
    task.save()
    return redirect("/")

def delete_task(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return redirect("/")

def update_task(request,pk):
    task=Task.objects.all(id=pk)
    if request.methof== "POST":
        title =request.POST.get("title")
        task.title =title
        title.save()
        return redirect("/")

    return render(request, "update.html", {"task": task})
        
    