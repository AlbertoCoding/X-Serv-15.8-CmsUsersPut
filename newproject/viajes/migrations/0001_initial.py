# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CLiente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
                ('dni', models.CharField(max_length=32)),
                ('nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Viaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('destino', models.CharField(max_length=32)),
                ('locomocion', models.CharField(max_length=32)),
                ('alojamiento', models.CharField(max_length=32)),
                ('precio', models.DecimalField(max_digits=12, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='viaje',
            field=models.ForeignKey(to='viajes.Viaje'),
        ),
    ]
