# Generated by Django 3.1.5 on 2021-02-09 16:09

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210123_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='url',
        ),
        migrations.AddField(
            model_name='portfolio',
            name='live_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='source_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=('update__month',)),
        ),
    ]
