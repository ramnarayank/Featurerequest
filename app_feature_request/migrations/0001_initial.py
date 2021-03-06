# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-07 01:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FeatureReq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('clientpriority', models.IntegerField()),
                ('target_date', models.DateTimeField()),
                ('productarea', models.CharField(max_length=100)),
                ('clients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_feature_request.clients')),
            ],
        ),
    ]
