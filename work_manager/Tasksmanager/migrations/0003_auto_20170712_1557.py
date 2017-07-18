# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tasksmanager', '0002_auto_20170712_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeveloperWorkTask',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('time_elasped_dev', models.IntegerField(default=None, verbose_name='Time Elasped', null=True, blank=True)),
                ('developer', models.ForeignKey(to='Tasksmanager.Developer', verbose_name='Developer')),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='developer1',
        ),
        migrations.RemoveField(
            model_name='task',
            name='developer2',
        ),
        migrations.AddField(
            model_name='task',
            name='developers',
            field=models.ManyToManyField(to='Tasksmanager.Developer', verbose_name='Second Developer', related_name='dev1', null=True),
        ),
        migrations.AddField(
            model_name='developerworktask',
            name='task',
            field=models.ForeignKey(to='Tasksmanager.Task', verbose_name='Developer'),
        ),
    ]
