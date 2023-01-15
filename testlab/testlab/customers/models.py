from django.db import models
from django.utils.text import slugify


class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.pk}')

        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
