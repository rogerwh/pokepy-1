from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=20, verbose_name="Nombre")
    weight = models.SmallIntegerField()
    height = models.SmallIntegerField()
    types = models.ManyToManyField("api.PokeType")
    abilities = models.ManyToManyField("api.PokeAbility")

    def __str__(self):
        return self.name


class PokeType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Tipo")
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class PokeAbility(models.Model):
    name = models.CharField(max_length=50, verbose_name="Habilidades")
    description = models.TextField()

    def __str__(self):
        return self.name
