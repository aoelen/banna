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
        ('Januari', 'Januari'),
        ('Februari', 'Februari'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),
        ('July', 'July'),
        ('August', 'August'),
        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    )

    name = models.CharField(max_length=10, choices=MONTHS)
    year = models.ForeignKey("Year", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name) + " " + str(self.year.name)