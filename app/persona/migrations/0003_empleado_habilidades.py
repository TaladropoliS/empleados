# Generated by Django 3.2 on 2022-01-21 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_auto_20220121_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(related_name='empleado_habilidades', to='persona.Habilidades'),
        ),
    ]
