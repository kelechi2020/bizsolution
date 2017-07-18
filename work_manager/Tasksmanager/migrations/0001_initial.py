# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('client_name', models.CharField(max_length=1000, verbose_name='Client Name')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.CharField(max_length=1000, verbose_name='Description')),
                ('time_elasped', models.IntegerField(null=True, blank=True, verbose_name='Elapsed Time', default=None)),
                ('importance', models.IntegerField(verbose_name='Importance')),
                ('project', models.ForeignKey(blank=True, verbose_name='Project', to='Tasksmanager.Project', null=True, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('login', models.CharField(max_length=25, verbose_name='Login')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('phone', models.CharField(null=True, max_length=20, blank=True, verbose_name='Phone Number', default=None)),
                ('born_date', models.DateField(null=True, blank=True, verbose_name='Born Date', default=None)),
                ('last_connection', models.DateTimeField(null=True, blank=True, verbose_name='Date Of Last Connection', default=None)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('years_seniority', models.IntegerField(verbose_name='Seniority', default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Of birthday')),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, to='Tasksmanager.UserProfile', serialize=False, parent_link=True, primary_key=True)),
            ],
            bases=('Tasksmanager.userprofile',),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, to='Tasksmanager.UserProfile', serialize=False, parent_link=True, primary_key=True)),
                ('specialization', models.CharField(max_length=50, verbose_name='Specialization')),
            ],
            bases=('Tasksmanager.userprofile',),
        ),
        migrations.AddField(
            model_name='task',
            name='app_user',
            field=models.ForeignKey(to='Tasksmanager.Developer', verbose_name='User'),
        ),
        migrations.AddField(
            model_name='developer',
            name='supervisor',
            field=models.ForeignKey(to='Tasksmanager.Supervisor', verbose_name='Supervisor'),
        ),
    ]
