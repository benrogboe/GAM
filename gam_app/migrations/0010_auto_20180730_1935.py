# Generated by Django 2.0.1 on 2018-07-30 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gam_app', '0009_auto_20180730_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='apellido_materno',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='apellido_paterno',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='fecha_de_nacimiento',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='segundo',
            field=models.CharField(blank=True, default='', max_length=200),
            preserve_default=False,
        ),
    ]