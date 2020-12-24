from modeltranslation.translator import TranslationOptions, register
from stories.models import Recipe


@register(Recipe)
class RecipeTranslation(TranslationOptions):
    fields = ('title', 'short_description', 'description',)