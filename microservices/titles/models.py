from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['id']


class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['id']


class Title(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название фильма')
    year = models.IntegerField(verbose_name='год выпуска')
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание фильма'
    )
    genre = models.ManyToManyField(Genre)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True)

    def __str__(self):
        return self.name
