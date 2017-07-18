from Tasksmanager.models import Project, Task, Supervisor, Developer
from django.shortcuts import render
from django.utils import timezone




def page(request,pk):
    #saving a new Supervisor
    new_supervisor = Supervisor(name="Guido van Rossum", login="python", password="password", last_connection=timezone.now(), email="python@python.com", specialization="python")
    new_supervisor.save()

    # saving a new developer
    new_developer = Developer(name="milcah", login="milcah", password="password",email="milcah@python.com", supervisor=new_supervisor )
    new_developer.save()

    # saving a new Task
    project_to_link = Project.objects.get(id=1)
    new_task = Task(title="Adding Relationships", description="Example of adding relatinship and saving it", time_elasped=2, importance=0,
                    project=project_to_link, developer=new_developer)
    new_task.save()
    return  render(request, 'en/public/index.html', {'action':'save relationship'})


