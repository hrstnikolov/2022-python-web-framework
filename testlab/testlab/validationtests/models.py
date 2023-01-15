from django.db import models

from testlab.specifications.models import Specification


# Create your models here.
class ValidationTest(models.Model):
    class FunctionalState(models.TextChoices):
        FUNCTIONAL_STATUS_A = 'A'
        FUNCTIONAL_STATUS_B = 'B'
        FUNCTIONAL_STATUS_C = 'C'
        FUNCTIONAL_STATUS_D = 'D'

    class ConnectionState(models.TextChoices):
        MONITORED = 'monitored'
        POWERED = 'powered'
        CONNECTED = 'connected'
        NOT_CONNECTED = 'not connected'

    name = models.CharField(
        max_length=200,
        null=False,
        blank=False,
    )
    specification = models.ForeignKey(
        to=Specification,
        on_delete=models.RESTRICT,
    )
    functional_state = models.TextField(
        max_length=10,
        choices=FunctionalState.choices,
    )
    connection_state = models.TextField(
        max_length=100,
        choices=ConnectionState.choices,
    )
    parameters = models.TextField()
