from django.db import models

class CrimeNumber(models.Model):
    year = models.IntegerField()
    saiga = models.IntegerField()
    red_book = models.IntegerField()
    others = models.IntegerField()
    total = models.IntegerField()

    def calculate_total(self):
        return (self.saiga + self.red_book + self.others)

class TakenItems(models.Model):
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