from django.db import models
from django.contrib.auth.models import User

class Zone(models.Model):
    zone = models.IntegerField()

    def __str__(self):
        zone_name = "Zone " + str(self.zone)
        return zone_name


class Farm(models.Model):
    name = models.CharField(max_length=30)
    farmer = models.ForeignKey(User, related_name="Farmer" ,on_delete=models.CASCADE)
    person_in_charge = models.ManyToManyField(User, related_name="PIC")
    total_tree_amount = models.IntegerField()
    zone = models.ManyToManyField("Zone")

    def __str__(self):
        return str(self.name)


class Yield(models.Model):
    yield_number = models.IntegerField()

    def __str__(self):
        return "Yield: " + str(self.yield_number)