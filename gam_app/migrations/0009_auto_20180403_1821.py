# Generated by Django 2.0.1 on 2018-04-03 18:21

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gam_app', '0008_auto_20180313_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagen',
            name='traducción',
            field=ckeditor.fields.RichTextField(blank=True)),
    ]
