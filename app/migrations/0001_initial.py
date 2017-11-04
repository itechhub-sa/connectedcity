# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-03 22:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_one', models.CharField(max_length=100)),
                ('line_two', models.CharField(max_length=100)),
                ('gps', models.CharField(max_length=60)),
                ('city', models.CharField(max_length=15)),
                ('province', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CaseManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('reason', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cell', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=150)),
                ('specializations', models.TextField(max_length=50)),
                ('job_desc', models.TextField(max_length=1000)),
                ('cell', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Faults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defect', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('data_submitted', models.DateTimeField(auto_now_add=True)),
                ('verification_score', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Address')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Citizen')),
            ],
        ),
        migrations.CreateModel(
            name='ReporterRewards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fault', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Faults')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Citizen')),
            ],
        ),
        migrations.CreateModel(
            name='Schedular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
                ('fault_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Faults')),
                ('recommended', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='TrustedReporters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trust_score', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Address')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Citizen')),
            ],
        ),
        migrations.AddField(
            model_name='casemanager',
            name='fault',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Faults'),
        ),
        migrations.AddField(
            model_name='casemanager',
            name='responder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Employee'),
        ),
    ]
