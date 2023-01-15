from django.db import models

from testlab.customers.models import Customer


class Specification(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        null=False,
        blank=False,
    )
    revision = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )
    customer = models.ForeignKey(
        to=Customer,
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return f'{self.name} {self.revision}, {self.customer}'
