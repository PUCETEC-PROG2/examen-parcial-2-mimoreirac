# Generated by Django 4.2 on 2025-01-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='synopsis',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('C', 'Comedia'), ('R', 'Romance'), ('A', 'Acción'), ('D', 'Drama'), ('T', 'Terror'), ('I', 'Infantil')], max_length=30),
        ),
    ]
