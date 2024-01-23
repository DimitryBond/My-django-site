from django.db import models

class Articles (models.Model):
    title = models.CharField("Название", max_length=50)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = "Main"
        verbose_name_plural = "Main"