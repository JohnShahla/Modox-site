from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"message created by {self.name}"
    