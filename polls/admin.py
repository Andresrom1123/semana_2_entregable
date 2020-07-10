from django.contrib import admin

# Register your models here.

from polls.models import Classroom, Student

admin.site.register(Classroom)
admin.site.register(Student)
