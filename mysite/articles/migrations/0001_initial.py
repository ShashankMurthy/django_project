# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('aurthor', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('category', models.CharField(max_length=140)),
                ('body', models.TextField()),
                ('image', models.ImageField(verbose_name='Label', upload_to='static/upload')),
            ],
        ),
    ]
