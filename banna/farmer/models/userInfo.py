from django.db import models
from django.contrib.auth.models import User

#information about a specific farm
class Farm(models.Model):
    name = models.CharField(max_length=30)
    farmer = models.ForeignKey(User, related_name="Farmer" ,on_delete=models.CASCADE)
    zone = models.ForeignKey("Zone", on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=9, decimal_places=6,null=True, blank = 'True')
    lng = models.DecimalField(max_digits=9, decimal_places=6,null=True, blank = 'True')

    def __str__(self):
        return str(self.name)
