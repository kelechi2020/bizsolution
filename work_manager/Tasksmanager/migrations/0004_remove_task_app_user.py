# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tasksmanager', '0003_auto_20170712_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='app_user',
        ),
    ]
