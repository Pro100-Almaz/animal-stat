from django.db import models

class CrimeNumber(models.Model):
    year = models.IntegerField()
    saiga = models.IntegerField()
    red_book = models.IntegerField()
    others = models.IntegerField()
    total = models.IntegerField()
    percentage = models.FloatField(max_length=3)

    def calculate_total(self):
        self.total = (int(self.saiga) + int(self.red_book) + int(self.others))

class TakenItems(models.Model):
    year = models.IntegerField()
    saiga_without_horns = models.IntegerField()
    saiga_with_horns = models.IntegerField()
    saiga_female = models.IntegerField()
    horns = models.IntegerField()
    segoltok = models.IntegerField()

    arhar = models.IntegerField()
    jeiran = models.IntegerField()
    drofa = models.IntegerField()
    qulan = models.IntegerField()
    sadja = models.IntegerField()
    falcon = models.IntegerField()
    podorlik = models.IntegerField()
    falcon_baloban = models.IntegerField()
    sturgeon = models.IntegerField()
    badger = models.IntegerField()

class Location(models.Model):
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=500)

class Animal(models.Model):
    name = models.CharField(max_length=50)
    number = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

