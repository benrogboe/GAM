# Generated by Django 2.0 on 2018-01-08 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gam_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='apellido_materno',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='apellido_paterno',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='portapapeles',
            name='imágenes',
            field=models.ManyToManyField(blank=True, to='gam_app.Imagen'),
        ),
    ]
