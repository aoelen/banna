from django.db import models

class Year(models.Model):
    YEAR = (
        ('2018', '2018'),
        ('2019', '2019'),
        ('2020', '2020'),
        ('2021', '2021'),
    )

    name = models.CharField(max_length=4, choices=YEAR)

    def __str__(self):
        return str(self.name)

class Month(models.Model):
    MONTHS = (
        ('01', 'Januari'),
        ('02', 'Februari'),
        ('03', 'March'),
        ('04', 'April'),
        ('05', 'May'),
        ('06', 'June'),
        ('07', 'July'),
        ('08', 'August'),
        ('09', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),
    )

    name = models.CharField(max_length=10, choices=MONTHS)
    year = models.ForeignKey("Year", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + " " + str(self.year.name)