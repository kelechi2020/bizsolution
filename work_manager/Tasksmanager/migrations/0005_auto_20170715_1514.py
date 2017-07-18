# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tasksmanager', '0004_remove_task_app_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developerworktask',
            name='task',
            field=models.ForeignKey(verbose_name='Task', to='Tasksmanager.Task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='developers',
            field=models.ManyToManyField(verbose_name='Second Developer', related_name='dev1', to='Tasksmanager.Developer'),
        ),
    ]
