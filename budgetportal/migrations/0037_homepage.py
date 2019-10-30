# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-30 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgetportal', '0036_auto_20191023_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Homepage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_heading', models.CharField(blank=True, max_length=1000)),
                ('sub_heading', models.CharField(blank=True, max_length=1000)),
                ('primary_button_label', models.CharField(blank=True, max_length=1000)),
                ('primary_button_url', models.CharField(blank=True, max_length=1000)),
                ('secondary_button_label', models.CharField(blank=True, max_length=1000)),
                ('secondary_button_url', models.CharField(blank=True, max_length=1000)),
                ('call_to_action_sub_heading', models.CharField(blank=True, max_length=1000)),
                ('call_to_action_heading', models.CharField(blank=True, max_length=1000)),
                ('call_to_action_link_label', models.CharField(blank=True, max_length=1000)),
                ('call_to_action_link_url', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]
