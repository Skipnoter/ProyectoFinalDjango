# Generated by Django 4.1.3 on 2022-12-22 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='fecha_de_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
