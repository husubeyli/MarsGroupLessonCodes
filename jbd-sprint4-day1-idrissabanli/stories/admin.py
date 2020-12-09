from django.contrib import admin
from stories.models import (
    Recipe,
    Author,
    Category, 
    Tag,
    Contact
)


admin.site.register(Recipe)
admin.site.register([Author, Category, Tag, Contact])
