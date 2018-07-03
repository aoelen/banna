from django.shortcuts import get_object_or_404, render, redirect

from farmer.models import Date, Farm, Report, Reports_Yield
from django.contrib.auth.models import User
from datetime import datetime, date
from time import strftime
from django.utils import translation

#SHOW OVERVIEW FARMS
def overview_farm(request, language_code):
    # If form is correct,post into database and return next page
    user_language = language_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    #check which user has which farms
    for loggedin_user in  User.objects.filter(id= request.user.id):
        farms = Farm.objects.filter(farmer=loggedin_user)

    #dict for the template
    context = {
        'farms': farms,
        'language': language_code
    }
    return render(request, 'farmer/overview/farms.html', context)
