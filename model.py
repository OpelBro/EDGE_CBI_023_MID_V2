from django.db import models
from django.utils import timezone

class Item(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
