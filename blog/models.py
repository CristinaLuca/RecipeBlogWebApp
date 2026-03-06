from django.db import models
from organiser.models import Recipe, Tag

# Create your models here.
class BlogPost (models.Model):
    #define the model fields. They are all Pythin classes
    postTitle = models.CharField(max_length=20)
    postText = models.TextField()
    publication_Date = models.DateField(
        auto_now_add = True, #the filed is automatically set to the current date the first time it is submitted
        unique_for_month = 'publication_Date' #ensure that the blog post for each month is unique
    )
    postSlug = models.SlugField(
        max_length=30,
        unique=True
    )

    # many-to-many relationships with Tag and Recipe
    tags = models.ManyToManyField(
        Tag,
        related_name = 'blog_posts'
        )

    recipes = models.ManyToManyField(
        Recipe,
        related_name = 'blog_posts'
        )
