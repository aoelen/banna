from django.db import models
from .userInfo import Farm
from .datesInfo import Month


class Yield(models.Model):
    yield_number = models.IntegerField()

    def __str__(self):
        return "Yield " + str(self.yield_number)

class Tree(models.Model):
    yield_id = models.ForeignKey("Yield", on_delete=models.CASCADE)
    planted_amount_trees = models.IntegerField()
    harvested_amount_kg_banana = models.IntegerField()
    harvested_amout_trees = models.IntegerField()
    farm = models.ForeignKey("Farm", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.farm.name) + ": " + str(self.yield_id)

class Report(models.Model):
    FERTILIZER_USED = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    used = models.CharField(max_length=30, choices=FERTILIZER_USED)
    amount = models.IntegerField(null=True, blank = 'True')

    yields_id = models.ManyToManyField(Yield)
    month = models.ForeignKey("Month", on_delete=models.CASCADE, null = 'True')
    farm = models.ForeignKey("Farm", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.farm.name) + " " + str(self.month.name) + " " + str(self.month.year)