# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_inputform_numberofsplotfiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputMaha',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('EnterQuerySize', models.IntegerField(verbose_name='Enter size of missing points.')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='inputform',
            name='EnterPoints',
            field=models.CharField(default=b'Choose File Size', max_length=5, verbose_name='Select File Size', choices=[(b'500MB', b'500MB'), (b'1GB', b'1GB'), (b'3GB', b'3GB'), (b'5GB', b'6GB')]),
        ),
        migrations.AlterField(
            model_name='inputform',
            name='EnterQuerySize',
            field=models.IntegerField(verbose_name='Enter size of Query to be generated'),
        ),
    ]
