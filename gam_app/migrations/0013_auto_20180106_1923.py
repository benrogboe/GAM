# Generated by Django 2.0 on 2018-01-06 19:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gam_app', '0012_document_dzi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='dzi',
        ),
        migrations.AlterField(
            model_name='document',
            name='ocr_text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
