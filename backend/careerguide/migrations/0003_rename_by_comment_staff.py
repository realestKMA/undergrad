# Generated by Django 3.2.9 on 2021-11-27 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('careerguide', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='by',
            new_name='staff',
        ),
    ]