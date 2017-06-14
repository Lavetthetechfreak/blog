# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('Title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('Timestamp', models.DateTimeField(auto_now=True)),
                ('Update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
