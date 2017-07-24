from django.shortcuts import render
from Tasksmanager.models import Task
from django.core.urlresolvers import reverse

def page(request):
    tasks_list = Task.objects.all()

    last_task = 0
    #in this line we define last_task variable

    if 'last_task' in request.session:
        #above line is used to check whether there is a session variable named last_task
        last_task = Task.objects.get(id = request.session['last_task'])

        tasks_list =tasks_list.exclude(id=request.session['last_task'])
        #we exclude the last task so the query set do not have duplicates
    return render(request, 'en/public/task_list.html', {'tasks_list': tasks_list, 'last_task': last_task})

