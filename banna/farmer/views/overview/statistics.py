from django.shortcuts import get_object_or_404, render, redirect
from farmer.models import Date, Farm, Report, Reports_Yield
from django.contrib.auth.models import User
from datetime import datetime, date
from time import strftime
from django.contrib.auth.decorators import user_passes_test
from farmer.views import auth_check
from django.utils import translation


def statistics(request, farm_id, language_code):
    user_language = language_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    bananas_harvested = 0
    trees_planted = 0
    trees_harvested = 0
    yields = Reports_Yield.objects.filter(report_id__farm__id=farm_id);
    print(yields)

    for report_yield in yields:
        bananas_harvested = bananas_harvested + report_yield.harvested_amount_kg_banana
        trees_planted = trees_planted + report_yield.planted_amount_trees
        trees_harvested = trees_harvested + report_yield.harvested_amount_trees


    context = {
        'farm_id' : farm_id,
        'bananas_harvested': bananas_harvested,
        'trees_planted': trees_planted,
        'trees_harvested': trees_harvested

    }
    return render(request, 'farmer/overview/statistics.html', context)
