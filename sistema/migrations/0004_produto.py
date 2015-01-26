# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_auto_20150122_0355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_produto', models.CharField(max_length=64, verbose_name=b'Nome do produto')),
                ('valor', models.CharField(max_length=64, verbose_name=b'Valor do produto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
