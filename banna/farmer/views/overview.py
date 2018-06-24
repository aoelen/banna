from django.shortcuts import get_object_or_404, render, redirect

from farmer.models import Month, Farm, Report
from django.contrib.auth.models import User


#SHOW OVERVIEW DATA MONTH
def overview_month(request, id=id):
    print (str((User.objects.all())))
    # for i in User.objects.all():
    #     print (type(i))
    #     if 'aron' == i:
    #         print('yes')

    reports = Report.objects.all()
    return render(request, 'farmer/overview.html', {'reports': reports})