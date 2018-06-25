from django.contrib import admin
from farmer.models import *


# Register your models here.
admin.site.register(Farm)
admin.site.register(Report)
admin.site.register(Zone)
admin.site.register(Month)
admin.site.register(Year)
admin.site.register(Reports_Yield)

# admin.site.register(Tree)
# admin.site.register(Yield)
