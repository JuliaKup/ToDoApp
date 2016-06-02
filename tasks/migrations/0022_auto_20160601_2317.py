# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-01 23:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0021_auto_20160601_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task'),
        ),
        migrations.AlterField(
            model_name='task',
            name='doer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='executors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasks.Project'),
        ),
    ]
