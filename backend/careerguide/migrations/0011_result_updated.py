# Generated by Django 3.2.9 on 2022-03-11 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerguide', '0010_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Updated'),
        ),
    ]
