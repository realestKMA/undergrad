# Generated by Django 3.2.9 on 2021-12-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerguide', '0006_rename_comment_observation'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='categories',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='Categories'),
        ),
    ]