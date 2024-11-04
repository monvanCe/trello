from django.db import models
from django.utils.text import slugify
from user.models import User 
from category.models import Category



class Task(models.Model):
    title = models.CharField(max_length=255)  
    description = models.TextField(blank=True, null=True)  
    slug = models.SlugField(unique=True, blank=True)  
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    git = models.URLField()  
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  
        super().save(*args, **kwargs)
