# Generated by Django 2.0.1 on 2018-06-19 16:41

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gam_app', '0011_auto_20180619_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagen',
            name='archivo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gam_app.Archivo'),
        ),
        migrations.AlterField(
            model_name='imagen',
            name='colección',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gam_app.Colección'),
        ),
    ]