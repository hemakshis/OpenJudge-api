# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-24 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='auth_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=120)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('name', models.CharField(max_length=120)),
                ('username', models.CharField(max_length=120, primary_key=True, serialize=False)),
                ('role', models.CharField(choices=[('USER', 'USER'), ('ADMIN', 'ADMIN')], max_length=120)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='auth_user',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.user_data'),
        ),
    ]
