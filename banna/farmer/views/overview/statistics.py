from django.shortcuts import get_object_or_404, render, redirect
from farmer.models import Date, Farm, Report, Reports_Yield
from django.contrib.auth.models import User
from datetime import datetime, date
from time import strftime
from django.contrib.auth.decorators import user_passes_test
from farmer.views import auth_check

def statistics(request, farm_id):


    context = {
        'farm_id' : farm_id,

    }
    return render(request, 'farmer/overview/statistics.html', context)
