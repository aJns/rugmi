from django.contrib import admin

from .models import Submission, Comment

admin.site.register(Submission)
admin.site.register(Comment)
