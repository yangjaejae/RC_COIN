from django.contrib import admin
from .models import Notice

# Register your models here.

class NoticeAdmin(admin.ModelAdmin):
    model = Notice
    verbose_name_plural = 'notice'

admin.site.register(Notice, NoticeAdmin)

