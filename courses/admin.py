from django.contrib import admin

# Register your models here.
from courses.models import Course, Slide, Comment, CheckPoint

admin.site.register(Course)
admin.site.register(Slide)
admin.site.register(Comment)
admin.site.register(CheckPoint)
