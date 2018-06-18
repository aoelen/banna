from django.db import models

class Farmer(models.Model):
    id = models.CharField(max_length=30, default='')
    name = models.CharField(max_length=30, default='')
    phone_number = models.CharField(max_length=18, default='')
    total_hectare = models.CharField(max_length=30, default='')
    location = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.farmer_id


class Area(models.Model):
    id = models.CharField(max_length=30, default='')
    hectare = models.CharField(max_length=30, default='')
    tree_amount = models.CharField(max_length=30, default='')
    cycle = models.CharField(max_length=30, default='')
    start_date = models.DateTimeField(auto_now_add=True)

    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Harvest(models.Model):
    id = models.CharField(max_length=30, default='')
    amount_banana = models.CharField(max_length=30, default='')
    date = models.DateTimeField(auto_now_add=True)
    amount_wasted = models.CharField(max_length=30, default='')

    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Fertilizer(models.Model):
    name = models.CharField(max_length=30, default='')
    type = models.CharField(max_length=30, default='')
    date = models.DateTimeField(auto_now_add=True)
    amount = models.CharField(max_length=30, default='')

    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Remarks(models.Model):
    id = models.CharField(max_length=30, default='')
    type = models.CharField(max_length=30, default='')
    description = models.TextField(default='')
    date = models.DateTimeField(auto_now_add=True)

    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


#Examples which we maybe need to use
    # voice_label = models.ManyToManyField(VoiceLabel, blank=True)
    # image_url = models.URLField(null=True)
    # description = models.TextField(default='', blank=True)





