# Generated by Django 3.2.9 on 2021-12-28 21:52

import careerguide.others
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('username', models.CharField(help_text='<b>Students username syntax: department/class/reg_no</b><br><b>Staff username syntax: STF0000</b>', max_length=255, unique=True, verbose_name='Username')),
                ('other_name', models.CharField(blank=True, max_length=255, verbose_name='Other Name')),
                ('gender', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=6, null=True, verbose_name='Gender')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('image', models.ImageField(blank=True, null=True, upload_to=careerguide.others.save_image, verbose_name='Image')),
                ('about', models.TextField(blank=True, null=True, verbose_name='About me')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address')),
                ('phone_1', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone 1')),
                ('phone_2', models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone 2')),
                ('continent', models.CharField(blank=True, max_length=50, null=True, verbose_name='Continent')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Country')),
                ('state', models.CharField(blank=True, max_length=50, null=True, verbose_name='State')),
                ('postal', models.CharField(blank=True, max_length=50, null=True, verbose_name='Postal/ZIP code')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('reg_no', models.CharField(max_length=4, verbose_name='Reg no')),
                ('level', models.CharField(choices=[('jss1', 'jss1'), ('jss2', 'jss2'), ('jss3', 'jss3'), ('sss1', 'sss1'), ('sss2', 'sss2'), ('sss3', 'sss3')], max_length=4, verbose_name='Student level')),
                ('department', models.CharField(choices=[('art', 'art'), ('science', 'science'), ('commercial', 'commercial'), ('social science', 'social science')], max_length=255, verbose_name='Department')),
                ('parent', models.CharField(blank=True, max_length=255, null=True, verbose_name='Parent/Guardian')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.CharField(blank=True, max_length=7, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('staff_id', models.CharField(help_text='Example: <b>STF1234</b>', max_length=7, unique=True, verbose_name='Staff ID')),
                ('level', models.CharField(blank=True, max_length=255, null=True, verbose_name='Level')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
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
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Created')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('slug', models.SlugField(max_length=255, null=True, verbose_name='Title slug')),
                ('question', models.TextField(verbose_name='Question')),
                ('completed', models.BooleanField(default=False, verbose_name='Completed')),
                ('categories', models.CharField(blank=True, help_text='Comma/space seperated values representing the type of students this questionnaire is ment for<br>E.G: art, ss1, male', max_length=255, verbose_name='Categories')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='careerguide.staff')),
                ('students', models.ManyToManyField(related_name='questions', to='careerguide.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('detail', models.TextField(verbose_name='Details')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='Created')),
                ('staff', models.ForeignKey(help_text='The staff who made the comments.', on_delete=django.db.models.deletion.CASCADE, to='careerguide.staff')),
                ('student', models.ForeignKey(help_text='The student the comment is made for.', on_delete=django.db.models.deletion.CASCADE, to='careerguide.student')),
            ],
        ),
        migrations.AddConstraint(
            model_name='student',
            constraint=models.UniqueConstraint(fields=('reg_no', 'level', 'department'), name='unique student'),
        ),
    ]
