from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

class NewsContent(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    slug = models.SlugField(unique=True)

    is_published = models.BooleanField(default=False)  # Corrected field name
    publish_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
