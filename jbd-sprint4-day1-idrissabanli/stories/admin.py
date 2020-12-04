from django.contrib import admin
from stories.models import (
    Recipe,
    Author,
    Category, Tag
)


admin.site.register(Recipe)
admin.site.register([Author, Category, Tag ])
