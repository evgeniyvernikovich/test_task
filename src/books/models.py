from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(
        max_length= 80, 
        verbose_name="Название книги"
    )
    author = models.ManyToManyField(
        'authors.Author',
        verbose_name="Автор"
    )
    publication_date = models.DateField(verbose_name="Дата публикации")
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание"
    )

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name
    
    def get_absolute_url(self):
        return '/b_show'
    