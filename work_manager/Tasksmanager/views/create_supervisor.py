from django.shortcuts import render
from Tasksmanager.models import Supervisor
from django import forms
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def page(request):
    if len(request.POST) > 0:
        form = Form_supervisor(request.POST)
        if form.is_valid():
            form.save(commit=True)
            #if saving form is successful redirect to the specified url in the reverse function
            #reverse function is used to get the url from its definition in url.py
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'en/public/create_supervisor.html', {'form': form})
    else:
        form = Form_supervisor()
        return render(request, 'en/public/create_supervisor.html', {'form': form})


class Form_supervisor(forms.ModelForm):
    #class inherits from modelfolrm
    class Meta:
        model = Supervisor
        exclude = ('date_created', 'last_connection',) #exclude ust receive a tuple