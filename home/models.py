from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


class Portfolio(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)
    image = models.ImageField(upload_to='portfolio-images')
    description = models.TextField()
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

@receiver(post_save, sender=Portfolio)
def save_slug(sender, instance=None, created=False, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()

