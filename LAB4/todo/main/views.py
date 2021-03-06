from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from main.models import Main


class MainPage(generic.ListView):
    template_name = 'todos/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Main.objects.order_by('-time_cre')


def add(request):
    name = request.POST['title']
    Main.objects.create(name=name)
    return redirect('main:index')


def delete(request, id):
    todo = get_object_or_404(Main, pk=id)
    todo.delete()
    return redirect('main:completed_todo_list')


def update(request, id):
    todo = get_object_or_404(Main, pk=id)
    isCompleted = request.POST.get('finished', False)
    if isCompleted == 'on':
        isCompleted = True

    todo.finished = isCompleted

    todo.save()
    return redirect('main:completed_todo_list')


def index(request):
    return redirect('/todos')

class GetFinished(generic.ListView):
    template_name = 'todos/completed_todo_list.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Main.objects.filter(finished=True).order_by('-time_cre')
