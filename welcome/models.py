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

class AnimalName(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Location(models.Model):
    region = models.CharField(max_length=500)
    name = models.ForeignKey(AnimalName, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + " " + str(self.region)  

class AnimalData(models.Model):
    number = models.IntegerField(blank=True, null=True)
    year = models.IntegerField()
    animal = models.ForeignKey(Location, on_delete=models.CASCADE)




