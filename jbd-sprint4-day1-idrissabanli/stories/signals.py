from django.db.models.signals import pre_save
from django.utils.timezone import now
from django.dispatch import receiver
from stories.models import Recipe
from slugify import slugify


@receiver(pre_save, sender=Recipe)
def create_recipe(sender, instance, **kwargs):
    instance.slug = slugify(instance.title+str(now().strftime('%Y-%m-%d-%H-%M-%S')))

