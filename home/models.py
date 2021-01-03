from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.utils import timezone


class Portfolio(models.Model):
    TYPE_CHOICES = [('web', 'Web'), ('app', 'App')]
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True)
    image = models.ImageField(upload_to='portfolio-images')
    port_type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='web')
    description = models.TextField()
    url = models.URLField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

@receiver(post_save, sender=Portfolio)
def save_slug(sender, instance=None, created=False, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()

