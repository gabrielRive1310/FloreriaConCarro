# Generated by Django 3.0 on 2019-12-08 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Estado', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Flor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('valor', models.IntegerField()),
                ('descripcion', models.CharField(max_length=150)),
                ('stock', models.IntegerField()),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Estado')),
            ],
        ),
    ]
