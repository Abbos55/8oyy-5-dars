from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pages = models.PositiveIntegerField(default=1)
    published_year = models.SmallIntegerField(default=2020)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title
