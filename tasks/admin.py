from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from tasks.models import Task, Project, Comment, User

admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Comment)