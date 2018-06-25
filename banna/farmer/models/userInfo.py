from django.db import models
from django.contrib.auth.models import User

class Zone(models.Model):

    zone = models.CharField(max_length=8)

    def __str__(self):
        zone_name = "Zone " + str(self.zone)
        return zone_name


class Farm(models.Model):
    name = models.CharField(max_length=30)
    farmer = models.ForeignKey(User, related_name="Farmer" ,on_delete=models.CASCADE)
    person_in_charge = models.ManyToManyField(User, related_name="PIC")
    zone = models.ManyToManyField("Zone")

    def __str__(self):
        return str(self.name)

