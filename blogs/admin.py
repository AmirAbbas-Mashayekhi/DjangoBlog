from django.contrib import admin
from .models import Author, Blog


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["user_name"]


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "created_at", "modified_at", "status"]
