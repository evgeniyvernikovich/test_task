from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="ФИО автора"    
    )
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    country = models.CharField(max_length=40, verbose_name="Страна")
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
        return f'/a_detail/{self.pk}'

