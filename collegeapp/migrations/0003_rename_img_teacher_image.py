# Generated by Django 4.2.16 on 2024-10-24 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collegeapp', '0002_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='img',
            new_name='image',
        ),
    ]
