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


class Rendeles(models.Model):

    sorszam = models.IntegerField()
    termek = models.ForeignKey(Termek, on_delete=models.CASCADE)
    kartyae = models.BooleanField()
    rendeles_ideje = models.DateTimeField()
    elkeszult = models.BooleanField()

    class Meta:
        verbose_name = "Rendelés"
        verbose_name_plural = "Rendelések"

    def __str__(self):
        return f'{self.sorszam}: {self.termek} ({self.rendeles_ideje})' + ('✔' if self.elkeszult else '❌')