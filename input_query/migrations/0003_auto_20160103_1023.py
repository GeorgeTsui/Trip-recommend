# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('input_query', '0002_auto_20160103_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='num',
            field=models.IntegerField(),
        ),
    ]
