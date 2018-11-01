from django.contrib import admin
from .models import Board, Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    verbose_name_plural = 'comment'

class BoardAdmin(admin.ModelAdmin):
    model = Board
    verbose_name_plural = 'board'

admin.site.register(Board, BoardAdmin)
admin.site.register(Comment, CommentAdmin)