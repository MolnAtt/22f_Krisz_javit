from django.db import models

# Create your models here.

class Termek(models.Model):

    nev = models.CharField(max_length=255)
    ar = models.IntegerField()
    erzekenyseg = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Termék"
        verbose_name_plural = "Termékek"

    def __str__(self):
        return f'{self.nev} -- {self.ar} Ft'

