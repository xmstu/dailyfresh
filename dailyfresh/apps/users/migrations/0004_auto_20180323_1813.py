# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_testmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'verbose_name': '测试模型', 'verbose_name_plural': '测试模型'},
        ),
        migrations.RemoveField(
            model_name='testmodel',
            name='create_time',
        ),
        migrations.RemoveField(
            model_name='testmodel',
            name='delete',
        ),
        migrations.RemoveField(
            model_name='testmodel',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='testmodel',
            name='update_time',
        ),
        migrations.AddField(
            model_name='testmodel',
            name='status',
            field=models.SmallIntegerField(verbose_name='订单状态', default=1, choices=[(1, '待支付'), (2, '待发货'), (3, '待收货'), (4, '待评价'), (5, '已完成')]),
        ),
        migrations.AlterModelTable(
            name='testmodel',
            table='df_test',
        ),
    ]
