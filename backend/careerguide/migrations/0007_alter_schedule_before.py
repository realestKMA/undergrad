# Generated by Django 3.2.9 on 2021-12-31 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerguide', '0006_alter_schedule_before'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='before',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Before'),
        ),
    ]