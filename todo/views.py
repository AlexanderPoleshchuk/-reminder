from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.
def index(request):
    tasks = ToDo.objects.all()

    form = ToDoForm()
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks': tasks, 'form':form}
    return render(request, 'todo/base.html', context=context)