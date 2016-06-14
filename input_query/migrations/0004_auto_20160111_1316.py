# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input_query', '0003_auto_20160103_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('hotel_id', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=100000)),
            ],
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
    ]
