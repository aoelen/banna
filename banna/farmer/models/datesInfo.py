from django.db import models


class Date(models.Model):
    month = models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return str(self.name) + " " + str(self.month) + " " + str(self.year)