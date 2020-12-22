from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from stories.tools.validators import validate_email

User = get_user_model()


class Author(models.Model):
    CATEGORY_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )
    first_name = models.CharField('Name: ', max_length=30)
    last_name = models.CharField('Surname: ', max_length=40)
    username = models.CharField(("Username: "), max_length=50)
    email = models.EmailField("Email: ", max_length=254)
    password = models.CharField(max_length=50)
    gender = models.PositiveIntegerField(("Gender: "), choices=CATEGORY_CHOICES) # -
    address = models.CharField("Address: ", max_length=1024) # -
    biography = models.TextField(("Biograpyhy")) # -
    image = models.ImageField("Image: ", upload_to='media/users_images') # -
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
        verbose_name = ('User')
        verbose_name_plural = ('Users')
    def __str__(self):
        return self.first_name


class Tag(models.Model):
    title = models.CharField('Title', max_length=100, db_index=True)

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title


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
    # relations
    tags = models.ManyToManyField(Tag, related_name='recipes')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='recipes')

    # informations
    title = models.CharField('Basliq', max_length=100, db_index=True)
    slug = models.SlugField('Slug', editable=False, max_length=110, unique=True, )
    # category = models.PositiveSmallIntegerField('Kategoriya', choices=CATEGORY_CHOICES)
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

    def get_absolute_url(self):
        return reverse_lazy('stories:recipe_detail', kwargs={'slug': self.slug})


class Category(models.Model):
    title = models.CharField('Title', max_length=100, db_index=True)
    image = models.ImageField("Image Category: ", upload_to='media/categories_images')

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('-created_at', 'title')

    def __str__(self):
        return self.title


class RecipeComment(models.Model):
    # relations
    user = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='comments')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')

    # informations
    text = models.TextField('Text')
    
    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('-created_at',)

    def __str__(self):
        return self.user.first_name


class Contact(models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.EmailField('Email', max_length=40, validators=[validate_email, ])
    subject = models.CharField('Subject', max_length=255)
    message = models.TextField('Message')

    # moderations
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ('-created_at',)

    def __str__(self):
        return self.name