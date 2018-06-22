from django.db import models
from .userInfo import Yield, Farm
from .datesInfo import Month

class Planting(models.Model):
    amount_trees = models.IntegerField()
    month = models.ForeignKey(Month, on_delete=models.CASCADE,  null='True')
    yield_id = models.ForeignKey(Yield, on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

    def __str__(self):
        harvest_name = str(Farm.name) + ", Yield: " + str(Yield.yield_number)
        return harvest_name

class Harvest(models.Model):
    amount_kg_banana = models.IntegerField()
    amout_trees = models.IntegerField()
    month = models.ForeignKey(Month, on_delete=models.CASCADE, null='True')
    yield_id = models.ForeignKey(Yield, on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

    def __str__(self):
        harvest_name = str(Farm.name) + ", Yield: " + str(Yield.yield_number)
        return harvest_name

class Fertilizer(models.Model):
    FERTILIZER_USED = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    used = models.CharField(max_length=30, choices=FERTILIZER_USED)
    amount = models.IntegerField(null=True, blank = 'True')
    month = models.ForeignKey(Month, on_delete=models.CASCADE, null = 'True')
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)

    def __str__(self):
        fertilizer_name = str(Farm.name)
        return fertilizer_name



