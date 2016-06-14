# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input_query', '0004_auto_20160111_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('hotel_id', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=100000)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Hotels',
        ),
    ]
