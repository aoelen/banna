from django.db import models


class User(models.Model):
    ROLES = (
        ('farmer', 'Farmer'),
        ('agricultural_department', 'Agricultural department'),
        ('factory_owner', 'Factory owner'),
        ('pic', 'Person in Charge Farmer')
    )

    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    password = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=18, blank ='True')
    role = models.CharField(max_length=30, choices=ROLES)

    def __str__(self):
        user_name = str(self.first_name) + " " + str(self.surname)
        return user_name


class Zone(models.Model):
    zone = models.IntegerField()

    def __str__(self):
        zone_name = "Zone " + str(self.zone)
        return zone_name



class Farm(models.Model):
    name = models.CharField(max_length=30)
    farmer = models.ForeignKey("User", related_name="Farmer" ,on_delete=models.CASCADE)
    person_in_charge = models.ManyToManyField("User", related_name="PIC")
    total_tree_amount = models.IntegerField()
    zone = models.ManyToManyField("Zone")

    def __str__(self):
        return str(self.name)



class Yield(models.Model):
    yield_number = models.IntegerField()
    date = models.DateField(auto_now=True)
    farm = models.ForeignKey("Farm", on_delete=models.CASCADE)

    def __str__(self):
        yield_name = str(self.farm.name) + ": " + str(self.date) + ", Yield: " + str(self.yield_number)
        return yield_name



class Planting(models.Model):
    amount_trees = models.IntegerField()
    date = models.DateField(auto_now=True)
    yield_id = models.ForeignKey(Yield, on_delete=models.CASCADE)

    def __str__(self):
        harvest_name = str(self.yield_id.farm.name) + ": " + str(self.date) + ", Yield: " + str(self.yield_id.yield_number)
        return harvest_name



class Harvest(models.Model):
    amount_kg_banana = models.IntegerField()
    amout_trees = models.IntegerField()
    date = models.DateField(auto_now=True)
    yield_id = models.ForeignKey("Yield", on_delete=models.CASCADE)

    def __str__(self):
        harvest_name = str(self.yield_id.farm.name) + ": " + str(self.date) + ", Yield: " + str(self.yield_id.yield_number)
        return harvest_name



class Fertilizer(models.Model):
    FERTILIZER_USED = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    used = models.CharField(max_length=30, choices=FERTILIZER_USED)
    amount = models.IntegerField(null=True, blank = 'True')
    date = models.DateField(auto_now=True)
    farm = models.ForeignKey("Farm", on_delete=models.CASCADE)

    def __str__(self):
        fertilizer_name = str(self.farm.name) + ": " + str(self.date)
        return fertilizer_name




