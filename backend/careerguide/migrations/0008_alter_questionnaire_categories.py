# Generated by Django 3.2.9 on 2021-12-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careerguide', '0007_questionnaire_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaire',
            name='categories',
            field=models.CharField(blank=True, default='', help_text='Comma/space seperated values representing the type of students this questionnaire is ment for', max_length=255, verbose_name='Categories'),
        ),
    ]
