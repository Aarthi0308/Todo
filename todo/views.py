from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task

def addtask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

    
