from django.contrib import admin
from django.db import models
from django.db.models import fields
from modeltranslation.admin import TranslationAdmin
from stories.models import (
    Recipe,
    Author,
    Category, 
    Tag,
    Contact,
    RecipeComment
)

class CommentTabularInlineAdmin(admin.TabularInline):
    model = RecipeComment


@admin.register(Recipe)
class RecipeAdmin(TranslationAdmin):
    inlines = (CommentTabularInlineAdmin, )
    list_display = ('title',  'owner', 'category', 'is_published', 'created_at',)
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'owner__first_name', 'owner__last_name')
    ordering = ('-title',)
    # readonly_fields = ('title',)

    fieldsets = (
        ('Relations', {
            'description': 'This group informations for relations',
            'fields': ('owner', 'category', 'tags')
        }),
        ('Informations', {
            'description': 'This group for informations',
            'fields': ('title', 'short_description', 'description', 'image')
        }),
        ('Moderations', {
            'description': 'This group for moderations',
            'fields': ('is_published',),
            'classes': ('collapse',)
        }),
    )
        

admin.site.register([Author, Category, Tag, Contact, RecipeComment])
