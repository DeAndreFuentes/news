from django.contrib import admin
from .models import Articles, Comment


class CommentInline(admin.StackedInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Articles, ArticleAdmin)
admin.site.register(Comment)

# Register your models here.
