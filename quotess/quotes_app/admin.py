from django.contrib import admin
from .models import Author, Tag, Quote

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'born_date', 'born_location', 'description', 'created_at')
    search_fields = ('fullname', 'born_location')
    list_filter = ('born_date',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote', 'author', 'created_at')
    search_fields = ('quote', 'author__fullname')
    list_filter = ('tags', 'created_at')
