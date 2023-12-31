from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    body = models.TextField()
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.slug}"

    def get_absolute_url(self):
        return reverse('post:post-detail', args=(self.id, self.slug))
