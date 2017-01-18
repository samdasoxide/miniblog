from django.contrib import admin
from .models import Author, Blog, Comment


# Register your models here.
class CommentInstanceInline(admin.TabularInline):
    model = Comment
    readonly_fields = ('id',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'post_date')
    fields = ['title', ('author', 'post_date'), 'content']
    #inlines = [CommentInstanceInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'comment')

    # Don't show id and user (for now)
    fields = ['blog', 'comment']
