from django.conf.urls import include, url
from django.contrib import admin
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
    url(r'^create-supervisor$', 'Tasksmanager.views.create_supervisor.page', name="create-supervisor")

]
