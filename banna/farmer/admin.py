from django.contrib import admin
from farmer.models import *


# Register your models here.
admin.site.register(Farm)
admin.site.register(Report)
admin.site.register(Zone)
admin.site.register(Date)
admin.site.register(Reports_Yield)