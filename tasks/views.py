from django.shortcuts import render
from .models import Task


def task_list(request):
    title = request.GET.get('title')
    descrip = request.GET.get('descrip')
    stat = request.GET.get('stat')
    if title is not None and descrip is not None and stat is not None:
        Task.objects.create(
            title=title,
            descrip=descrip,
            stat=stat
        )
    posts = Task.objects.all()
    ctx = {'task': posts}
    return render(request, 'post/list.html', ctx)