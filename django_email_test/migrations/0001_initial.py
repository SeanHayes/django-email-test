# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now, help_text=b'The date you want to set as the date header.')),
                ('from_email', models.CharField(default=b'', max_length=254, verbose_name=b'from')),
                ('to', models.TextField(default=b'', blank=True)),
                ('bcc', models.TextField(default=b'', blank=True)),
                ('subject', models.CharField(default=b'This is a test email.', max_length=150)),
                ('body', models.TextField(default=b"Here's some default text.")),
                ('sent', models.BooleanField(default=False, editable=False)),
                ('error', models.TextField(default=b'', editable=False, blank=True)),
            ],
            options={
                'ordering': ['-added'],
            },
        ),
    ]
