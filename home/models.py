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
    created = models.DateField(default=timezone.now)
    updated = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

class Screenshot(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio-screenshots')

    def __str__(self):
        return "<Screenshot <{}>>".format(str(self.portfolio))


@receiver(post_save, sender=Portfolio)
def save_slug(sender, instance=None, created=False, **kwargs):
    if created:
        instance.slug = slugify(instance.title)
        instance.save()

