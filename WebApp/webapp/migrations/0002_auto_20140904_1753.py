# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inputform',
            old_name='points',
            new_name='EnterPoints',
        ),
        migrations.RenameField(
            model_name='inputform',
            old_name='querysize',
            new_name='EnterQuerySize',
        ),
        migrations.RenameField(
            model_name='inputform',
            old_name='split',
            new_name='NumberOfSplotFiles',
        ),
    ]
