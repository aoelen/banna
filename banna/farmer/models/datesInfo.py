from django.db import models

class Year(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)

class Month(models.Model):
    name = models.CharField(max_length=30)
    year = models.ForeignKey("Year", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + " " + str(self.year.name)