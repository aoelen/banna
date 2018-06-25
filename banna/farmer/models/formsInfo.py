from django.db import models
from .userInfo import Farm
from .datesInfo import Date

class Report(models.Model):
    FERTILIZER_USED = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    fertilizer_used = models.CharField(max_length=30, choices=FERTILIZER_USED)
    fertilizer_amount = models.IntegerField(null=True, blank = 'True')
    month = models.CharField(max_length=10, blank = 'True')
    year = models.IntegerField(blank = 'True')

    # month = models.ForeignKey("Date", on_delete=models.CASCADE, null = 'True')
    farm = models.ForeignKey("Farm", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.farm.name) + " " + str(self.month) + " " + str(self.year)

class Reports_Yield(models.Model):
    YIELDS = (
        ('Yield 1', 'Yield 1'),
        ('Yield 2', 'Yield 2'),
        ('Yield 3', 'Yield 3'),
        ('Yield 4', 'Yield 4'),
        ('Yield 5', 'Yield 5'),

    )
    report_id = models.ForeignKey("Report", on_delete=models.CASCADE)
    yield_number = models.CharField(max_length=7, choices=YIELDS)
    planted_amount_trees = models.IntegerField(null = 'True')
    harvested_amount_kg_banana = models.IntegerField(null = 'True')

    class Meta:
        unique_together = ('report_id', 'yield_number',)

    def __str__(self):
        return str(self.report_id) + ": " + str(self.yield_number)
