from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    tasks = ToDo.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todo/base.html', context=context)