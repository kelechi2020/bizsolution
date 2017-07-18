# - * - coding: utf -8 -*-


##bview for index page

from django.shortcuts import render

from Tasksmanager.models import Project
from django.db.models import Q

def page(request):
    new_project = Project(title="Task Manager With Django", description="Project to design a task manager for effective office management",
                           client_name ="Authur Eze Na Ukpo")
    new_project.save()
    all_projects = Project.objects.all()
    projects_by_filter = Project.objects.filter(client_name="Authur Eze Na Ukpo")
    return render(request, 'en/public/index.html', {"filter":projects_by_filter, "second_action":"display all Projects", "all_projects": all_projects} )