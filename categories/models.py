from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=75)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_projects(self):
        return self.project_set.all()