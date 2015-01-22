# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='nome_pessoa',
            field=models.CharField(max_length=64, verbose_name=b'Nome e sobrenome'),
        ),
    ]
