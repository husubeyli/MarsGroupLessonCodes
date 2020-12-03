from django.db import models


class Recipe(models.Model):
    """
    Bu Model reseptler ucun meselen Alma piroqu, ...
    """
    CATEGORY_CHOICES = (
        (1, 'Dessert'),
        (2, 'Drink'),
        (3, 'Isti yemek'),
        (4, 'Sulu yemek'),
    )
    title = models.CharField('Basliq', max_length=100, db_index=True)
    slug = models.SlugField('Slug', max_length=110)
    category = models.PositiveSmallIntegerField('Kategoriya', choices=CATEGORY_CHOICES)
    short_description = models.CharField('Qisa Mezmun', max_length=255)
    description = models.TextField('Mezmun', null=True, blank=True)
    image = models.ImageField('Sekil', upload_to='media/recipe_images')

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'recipes'
        verbose_name = 'Resept'
        verbose_name_plural = 'Reseptler'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title



