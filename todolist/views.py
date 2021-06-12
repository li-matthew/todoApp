from django.shortcuts import render, redirect
from .models import TodoList, Category
from django.contrib import messages
from django.utils import timezone, dateformat

# Create your views here.
def index(request):
    todos = TodoList.objects.all()
    categories = Category.objects.all()
    if request.method == 'POST':
        if 'taskAdd' in request.POST:
            title = request.POST['description']
            date = str(request.POST['date'])
            category = request.POST['categorySelect']
            content = title + ' -- ' + date + ' ' + category
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category), complete=False)
            Todo.save()
            return redirect('/')
        if 'taskDelete' in request.POST:
            checkedList = request.POST.getlist('checkedBox')
            if len(checkedList) > 0:
                for todoId in checkedList:
                    todo = TodoList.objects.get(id=int(todoId))
                    todo.delete()
        if 'taskComplete' in request.POST:
            checkedList = request.POST.getlist('checkedBox')
            if len(checkedList) > 0:
                for todoId in checkedList:
                    todo = TodoList.objects.get(id=int(todoId))
                    todo.complete = True
                    todo.save()
    return render(request, 'index.html', {'todos': todos.order_by('complete'), 'categories': categories, 'date': dateformat.format(timezone.now().date(), 'Y-m-d')})
