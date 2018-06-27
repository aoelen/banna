from django.shortcuts import get_object_or_404, render, redirect

from farmer.models import Date, Farm, Report, Reports_Yield
from django.contrib.auth.models import User
from datetime import datetime, date
from time import strftime


#SHOW OVERVIEW FARMS
def overview_farm(request):
    for loggedin_user in  User.objects.filter(id= request.user.id):
        farms = Farm.objects.filter(farmer=loggedin_user)
    return render(request, 'farmer/overview/farms.html', {'farms': farms})
