from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(
        verbose_name="Country",
        max_length=20
    )
    def __str__(self):
        return str(self.pk) + " " + self.name

class Author(models.Model):
    country = models.ForeignKey(
        "spravochniki.Country",
        on_delete=models.PROTECT,
        verbose_name="Country",
        default=1,
        related_name="authors"
    )
    name = models.CharField(
        verbose_name="Author name",
        max_length=20
    )
    description = models.TextField(
        verbose_name="Author description",
        null=True,
        blank=True
    )
    def __str__(self):
        return str(self.pk) + " " + self.name

class Book(models.Model):
    author = models.ForeignKey(
        "spravochniki.Author",
        on_delete=models.PROTECT,
        verbose_name="Author",
        related_name="books"
    )
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
