from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from . import models
from . models import Todo
from django.utils import timezone

# Create your views here.
def home(request):
    todo_items=Todo.objects.all().order_by('-created_at')
    return render(request, 'Todo/home.html',{'todo_items':todo_items})


def add_todo(request):
    content=request.POST['content']
    created_at=timezone.now()
    models.Todo.objects.create(text=content,created_at=created_at)
    return HttpResponseRedirect("/")
    

def delete_todo(request,todo_id):
    models.Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")





