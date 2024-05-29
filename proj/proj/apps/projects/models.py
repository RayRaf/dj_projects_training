from django.db import models

# Create your models here.
class Project(models.Model):
    tag = models.CharField('Код', max_length=100)

    def __str__(self) -> str:
        return self.tag
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'