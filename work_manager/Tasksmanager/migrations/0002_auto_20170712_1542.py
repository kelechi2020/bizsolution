# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tasksmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='developer1',
            field=models.ForeignKey(null=True, to='Tasksmanager.Developer', verbose_name='first user', related_name='dev1'),
        ),
        migrations.AddField(
            model_name='task',
            name='developer2',
            field=models.ForeignKey(null=True, to='Tasksmanager.Developer', verbose_name='first user', related_name='dev2'),
        ),
        migrations.AlterField(
            model_name='task',
            name='app_user',
            field=models.ForeignKey(verbose_name='Developer', to='Tasksmanager.Developer'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='login',
            field=models.CharField(max_length=25, verbose_name='Username'),
        ),
    ]
