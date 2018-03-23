# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='delete',
            field=models.SmallIntegerField(default=False, verbose_name='是否删除'),
        ),
        migrations.AlterField(
            model_name='user',
            name='delete',
            field=models.SmallIntegerField(default=False, verbose_name='是否删除'),
        ),
    ]
