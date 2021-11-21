from .forms import ProfileCreationForm, ProfileChangeForm, StaffAdminForm, StudentAdminForm
from .models import Profile, Staff, Student, Schedule, Questionnaire
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin


# Register your inline admins here.
class QuestionnaireInlineAdmin(admin.TabularInline):
    model = Questionnaire.students.through
    extra = 0


class ScheduleInlineAdmin(admin.TabularInline):
    model = Schedule

    fieldsets = (
        ("Identification", {"fields": ("id", "staff")}),
        ("Details", {"fields": ("title", "slug", "detail", "created", "completed")}),
    )

    extra = 0
    readonly_fields = ("id", "slug", "created")



# Register your models here.
class ProfileAdmin(UserAdmin):
    # forms to add and change a user
    form = ProfileChangeForm
    add_from = ProfileCreationForm

    # fields used in displaying the user model
    list_display = ('info', 'id', 'username',)
    list_filter = ('is_staff', 'is_active', 'is_superuser')
    list_display_links = ("info", "id",)

    fieldsets = (
        ("Identification", {"fields": ("id", "username", "password")}),
        ("Bio", {"fields": ("first_name", "other_name", "last_name", "gender", "dob", "about", "image")}),
        ("Contact", {"fields": ("email", "phone_1", "phone_2",)}),
        ("Address", {"fields": ("continent", "country", "state", "postal",)}),
        ("Dates", {"fields": ("date_joined", "last_login",)}),
        ("Permissions", {"fields": (("is_active", "is_staff", "is_superuser"), "user_permissions")}),
        ("Groups", {"fields": ("groups",)}),
    )
    
    # fields to render when creating a new user from the admin page
    add_fieldsets = (
        ("Identity", {"fields": ("username", "email",)}),
        ("Security", {"fields": ("password1", "password2",)}),
    )

    readonly_fields = ("id", "date_joined", "last_login")
    ordering = ("-is_staff", "-date_joined",)
    empty_value_display = '-empty-'


class StaffAdmin(admin.ModelAdmin):
    """
    Staff model admin settings/view
    """
    model = Staff
    form = StaffAdminForm
    
    list_display = ("id", "staff_name", "staff_id",)
    list_display_links = ("staff_name", "staff_id",)
    list_filter = ("level",)

    fieldsets = (("Identification", {"fields": ("id", "staff_id", "level", "profile")}),)
    
    ordering = ("id",)
    readonly_fields = ("id",)
    empty_value_display = '-empty-'
    inlines = [ScheduleInlineAdmin,]



class StudentAdmin(admin.ModelAdmin):
    """
    Student model admin settings/view
    """
    model = Student
    form = StudentAdminForm

    list_display = ("id", "student_name", "reg_no", "level", "department")
    list_display_links = ("reg_no", "student_name", "reg_no",)
    list_filter = ("level", "department")

    fieldsets = (
        ("Identification", {"fields": ("id", "reg_no", "level", "department")}),
        ("Bio", {"fields": ("parent", "profile")})
    )

    ordering = ("id",)
    readonly_fields = ("id",)
    empty_value_display = '-empty-'
    inlines = [QuestionnaireInlineAdmin,]



class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("id", "staff", "title", "created", "completed")
    list_display_links = ("staff", "title")
    list_filter = ("staff", "completed")

    fieldsets = (
        ("Identification", {"fields": ("id", "staff")}),
        ("Details", {"fields": ("title", "slug", "detail", "created", "completed")}),
    )

    ordering = ("-created",)
    readonly_fields = ("id", "slug", "created")
    

class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "staff", "completed")
    list_display_links = ("staff", "title")
    list_filter = ("staff", "completed")

    fieldsets = (
        ("Identification", {"fields": ("id", "staff")}),
        ("Detail", {"fields": ("title", "slug", "question", "created", "completed")}),
        ("Students", {"fields": ("students",)})
    )

    ordering = ("-created",)
    readonly_fields = ("id", "slug", "created")



admin.site.register(Staff, StaffAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)