# Generated by Django 5.1 on 2024-08-23 13:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('body', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(unique=True)),
                ('is_published', models.BooleanField(default=False)),
                ('publish_time', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
