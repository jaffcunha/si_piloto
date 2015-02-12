# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0004_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pergunta_enquete', models.CharField(max_length=128, verbose_name=b'Digite a pergunta da sua enquete')),
                ('num_alternativas', models.IntegerField(max_length=128, verbose_name=b'Quantas alternativas sua pergunta tera?')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('opcao', models.CharField(max_length=64, verbose_name=b'Alternativa')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='data_fim',
            field=models.DateField(verbose_name=b'Fim do projeto (dd/mm/aaaa)'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='data_inicio',
            field=models.DateField(verbose_name=b'Inicio do projeto (dd/mm/aaaa)'),
        ),
    ]
