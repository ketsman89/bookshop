from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(
        verbose_name="Book name",
        max_length=20
    )
    description = models.TextField(
        verbose_name="Book description",
        null=True,
        blank=True
    )

    created = models.DateTimeField(
        verbose_name="Created datetime",
        auto_now=False,
        auto_now_add=True
    )

    updated = models.DateTimeField(
        verbose_name="Updated datetime",
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return str(self.pk) + " " + self.name
