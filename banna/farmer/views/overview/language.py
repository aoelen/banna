from django.shortcuts import get_object_or_404, render, redirect

from farmer.models import Date, Farm, Report, Reports_Yield
from django.contrib.auth.models import User
from datetime import datetime, date
from time import strftime
from django.utils import translation

#SHOW OVERVIEW FARMS
def choose_language(request):
    #post the languague which user will use in the application
    if request.method == "POST":
        chosen_language = request.POST.get('language')
        return redirect('/farmer/'+ str(chosen_language) +'/farms/')
    return render(request, 'farmer/overview/language.html')
