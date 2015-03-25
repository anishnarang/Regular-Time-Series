# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.BigIntegerField()),
                ('querysize', models.IntegerField()),
                ('split', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
