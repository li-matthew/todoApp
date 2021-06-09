from django.shortcuts import render, redirect
from .models import TodoList, Category

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
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category))
            Todo.save()
            return redirect('/')
        if 'taskDelete' in request.POST:
            checkedList = request.POST['checkedBox']
            for todoId in checkedList:
                todo = TodoList.objects.get(id=int(todoId))
                todo.delete()
    return render(request, 'index.html', {'todos': todos, 'categories': categories})
