import re
from django.shortcuts import render,redirect
from .models import Task
from .forms import TasksForm

# Create your views here.

def todolist(request):

    tasks = Task.objects.all()
    form = TasksForm()
    context = {'tasks':tasks,'form':form}
    
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request,'main/todolist.html',context)

def update(request, pk):
    task = Task.objects.get(id=pk)
    form = TasksForm(instance=task)
    context = {'form':form}
    if request.method == 'POST':
        form = TasksForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'main/update.html',context)

def delete(request,pk):
    item = Task.objects.get(pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request,'main/delete.html',context={'item':item})