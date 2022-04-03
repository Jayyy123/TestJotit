from turtle import stamp, title
from django.db import models
import uuid


class Jotter(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, default='JotIT')
    snippet = models.CharField(max_length=200, blank=False, null=False, default='JotIT')
    detail = models.TextField(blank=False, null=False, default='JotIT')
    important = models.BooleanField(default=False)
    stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True,unique=True, editable=False)

    def __str__(self) -> str:
        return self.title