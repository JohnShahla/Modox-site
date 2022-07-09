import os

from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager

from categories.models import Categories

def get_upload_path(instance, filename):
    return os.path.join(instance.project.slug, filename)

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='PortfolioApp/uploads', null=True, blank=True)

    slug = models.SlugField(unique=True, max_length=120, blank=True)

    website_url = models.URLField(null=True, blank=True)

    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    tags = TaggableManager(blank=True)

    views = models.PositiveIntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']

    def get_absolute_url(self):
        return reverse("main:details", kwargs={"slug": self.slug})

    def get_views(self):
        return self.views


class ProjectImages(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_upload_path, null=True, blank=True)

    def __str__(self):
        return f"{self.project.name} {self.image.url}"

    class Meta: 
        verbose_name = "ProjectImage"
        verbose_name_plural = "Project Images"
    
