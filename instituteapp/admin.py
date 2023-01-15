from django.contrib import admin
from .models import Courses
# Register your models here.
class AdminCourses(admin.ModelAdmin):
    list_display = ['courses_name', 'fee', 'duration','start_date','trainer_name','trainer_exp','training_mode' ]

admin.site.register(Courses,AdminCourses)