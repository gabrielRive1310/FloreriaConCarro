# Generated by Django 2.2.7 on 2019-12-18 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='flor',
            name='idFlor',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flor',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]