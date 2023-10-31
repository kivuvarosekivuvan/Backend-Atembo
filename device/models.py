
import uuid
from django.db import models

class Device(models.Model):
    name = models.CharField(max_length=255)
    serial_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name
