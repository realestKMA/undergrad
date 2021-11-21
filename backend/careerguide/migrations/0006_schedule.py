# Generated by Django 3.2.9 on 2021-11-20 18:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('careerguide', '0005_auto_20211119_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, null=True, verbose_name='Title slug')),
                ('detail', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Created')),
                ('completed', models.BooleanField(default=False, verbose_name='Completed')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='careerguide.staff')),
            ],
        ),
    ]
