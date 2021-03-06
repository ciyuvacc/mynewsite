# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phonelist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sku', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
                ('qty', models.IntegerField()),
            ],
        ),
    ]
