from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import CreateView, DetailView
from Tasksmanager.models import Project, Task, Developer
from django.views.generic.list import ListView
from Tasksmanager.views.cbv import listviews, DetailView, developerDetailView
admin.autodiscover()
urlpatterns = [
    # Examples:
    # url(r'^$', 'work_manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin', include(admin.site.urls)),
    url(r'^$', 'Tasksmanager.views.index.page', name="index"),
    url(r'^index$', 'Tasksmanager.views.index.page'),
    url(r'^connection-Tasksmanager$', 'Tasksmanager.views.connection.page', name="connection"),
    url(r'^project-detail-(?P<pk>\d+)$', 'Tasksmanager.views.project_details.page', name="project_detail"),
    url(r'^create-developer$', 'Tasksmanager.views.create_developer.page', name="create-developer"),
    url(r'^create-supervisor$', 'Tasksmanager.views.create_supervisor.page', name="create-supervisor"),
    url(r'^create-project$', CreateView.as_view(model=Project, template_name="en/public/create_project.html", success_url='index', fields = ['title', 'description']), name="create-project"),
    url(r'^create-task$', CreateView.as_view(model=Task, template_name="en/public/create_task.html", success_url='index', fields = ['title','developers','description','project'] ), name='create-task'),
    url(r'^project-list$', listviews.Project_list.as_view(),name = "project-list"),
    url(r'^developer-list$', ListView.as_view(model=Developer, template_name="en/public/developer_list.html", paginate_by=4), name="developer-list"),
    url(r'^task_detail_(?P<pk>\d+)$', DetailView.Task_list.as_view(), name="task-detail"),
    url(r'^developer-details-(?P<pk>\d+)$',developerDetailView.Developer_detail.as_view(), name='developer-detail')
]
