from django.db import models
from froala_editor.fields import FroalaField

from django.contrib.auth.models import User
from .helper import (
    generate_slug
)

import readtime

# Create your models here.
class BlogModel(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    subtitle = models.CharField(max_length=1000, blank=True, null=True, default='')
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to="BlogImage")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def get_readtime(self):
        result = readtime.of_html(self.content)
        return result.text

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)
