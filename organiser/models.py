from django.db import models

# Create your models here.
class Tag (models.Model):
     #define the model fields. They are all Python classes
    tagName = models.CharField(max_length=30)
    tagSlug = models.SlugField(
        max_length=30,
        unique=True
    )

    #method that returns the tagName
    def __str__(self):
        return self.tagName



class Recipe (models.Model):
    #define the model fields. They are all Python classes
    name = models.CharField(max_length=30)
    description = models.TextField()
    ingredients = models.TextField()
    method = models.TextField()
    recipeSlug = models.SlugField(
         max_length=30,
        unique=True
    )

    # many-to-many relationship with Tag
    tags = models.ManyToManyField(Tag)




