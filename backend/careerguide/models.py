from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from .others import make_id, save_image
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings
from django.db import models
import uuid

# needed data
SEX: tuple = (('male', 'male'), ('female', 'female'))
STUDENT_LEVELS: tuple = (
    ('jss1', 'jss1'),
    ('jss2', 'jss2'),
    ('jss3', 'jss3'),
    ('sss1', 'sss1'),
    ('sss2', 'sss2'),
    ('sss3', 'sss3'),
)
DEPT: tuple = (
    ('art', 'art'),
    ('science', 'science'),
    ('commercial', 'commercial'),
    ('social science', 'Social Science'),
)


# Create your models here.
class Profile(AbstractUser):
    """
    My custom user model
    """

    # user identification
    id = models.UUIDField(_("ID"), primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    username = models.CharField(_("Username"), max_length=255, unique=True, blank=False, null=False)

    # user bio
    other_name = models.CharField(_("Other Name"), max_length=255, blank=True, null=False)
    gender = models.CharField(_("Gender"), max_length=6, choices=SEX, blank=True, null=True)
    dob = models.DateField(_("Date of Birth"), auto_now=False, auto_now_add=False, blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to=save_image, blank=True, null=True)
    about = models.TextField(_("About me"), blank=True, null=True)

    # user contact information
    email = models.EmailField(_("Email Address"), max_length=254, blank=True, null=True)
    phone_1 = models.CharField(_("Phone 1"), max_length=20, blank=True, null=True)
    phone_2 = models.CharField(_("Phone 2"), max_length=20, blank=True, null=True)

    # user location
    continent = models.CharField(_("Continent"), max_length=50, blank=True, null=True)
    country = models.CharField(_("Country"), max_length=50, blank=True, null=True)
    state = models.CharField(_("State"), max_length=50, blank=True, null=True)
    postal = models.CharField(_("Postal/ZIP code"), max_length=50, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)


    def __str__(self):
        if self.is_staff:
            return F"[STAFF] - {self.get_full_name()} : {self.id}"
        else:
            return F"[STUDENT] - {self.get_full_name()} : {self.id}"


    def info(self) -> str:
        if self.is_staff:
            return F"[STAFF] - {self.first_name or ''} {self.other_name or ''} {self.last_name or ''}"
        return F"[STUDENT] - {self.first_name or ''} {self.other_name or ''} {self.last_name or ''}"



class Staff(models.Model):
    """
    Staff model
    """
    id = models.CharField(_("ID"), max_length=7, primary_key=True, unique=True, blank=True, null=False)
    staff_id = models.CharField(_("Staff ID"), max_length=7, unique=True, blank=False, null=False, help_text=_("Example: <b>STF1234</b>"))
    level = models.CharField(_("Level"), max_length=255, blank=True, null=True)
    profile = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.id = self.staff_id
        super().save(*args, **kwargs)

    def __str__(self):
        return F"STAFF ID: {self.staff_id}"

    def staff_name(self):
        return F"{self.profile.first_name or ''} {self.profile.other_name or ''} {self.profile.last_name or ''}"
    


class Student(models.Model):
    """
    Students model
    """
    id = models.CharField(_("ID"), max_length=4, primary_key=True, unique=True, blank=True, null=False)
    reg_no = models.CharField(_("Reg no"), max_length=4, blank=False, null=False)
    level = models.CharField(_("Student level"), max_length=4, choices=STUDENT_LEVELS, blank=False, null=False)
    department = models.CharField(_("Department"), max_length=255, choices=DEPT, blank=False, null=False)
    parent = models.CharField(_("Parent/Guardian"), max_length=255, blank=True, null=True)
    profile = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            # every student have a unique reg no in a particular level and department.
            # so we made the fields reg_no, level, and departmanet unique.
            models.UniqueConstraint(fields=['reg_no', 'level', 'department'], name='unique student')
        ]

    def save(self, *args, **kwargs):
        self.id = int(self.reg_no)
        super().save(*args, **kwargs)

    def __str__(self):
        return F"{self.reg_no} - {self.level.upper()} {self.department.upper()}"

    def student_name(self):
        return F"{self.profile.first_name or ''} {self.profile.other_name or ''} {self.profile.last_name or ''}"

    

class Schedule(models.Model):
    """
    Schedule model for staffs to keep a todo task(s)
    a staff can have more than one schedule.
    """
    id = models.AutoField(_("ID"), primary_key=True, unique=True, blank=False, null=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=255, blank=False, null=True)
    slug = models.SlugField(_("Title slug"), max_length=255, blank=False, null=True)
    detail = models.TextField(_("Details"), blank=True, null=True)
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=False, default=timezone.now, blank=False, null=True)
    completed = models.BooleanField(_("Completed"), default=False, blank=False, null=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return F"{self.title}"
    


class Questionnaire(models.Model):
    """
    Questionnaire model for staffs to create questions for students.
    """
    id = models.AutoField(_("ID"), primary_key=True, unique=True, blank=False, null=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name="questions")
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=False, default=timezone.now, blank=False, null=True)
    title = models.CharField(_("Title"), max_length=255, blank=False, null=True)
    slug = models.SlugField(_("Title slug"), max_length=255, blank=False, null=True)
    question = models.TextField(_("Question"))
    completed = models.BooleanField(_("Completed"), default=False, blank=False, null=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return F"{self.title}"
    


class Comment(models.Model):
    """
    Model to store comments and observation on a particular students
    sessioin.
    """
    id = models.AutoField(_("ID"), primary_key=True, unique=True, blank=False, null=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, help_text=_("The staff who made the comments."))
    student = models.ForeignKey(Student, on_delete=models.CASCADE, help_text=_("The student the comment is made for."))
    detail = models.TextField(_("Details"))
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=False, default=timezone.now, blank=False, null=True)

    def __str__(self):
        return F"@{self.student}"