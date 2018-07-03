from django.shortcuts import get_object_or_404, render, redirect
from farmer.models import Date, Farm, Report, Reports_Yield
from django.contrib.auth.models import User
from datetime import datetime, date
from time import strftime
from django.contrib.auth.decorators import user_passes_test
from farmer.views import auth_check
from django.utils import translation
from django.utils.translation import gettext as _


def statistics(request, farm_id, language_code):
    # If form is correct,post into database and return next page
    user_language = language_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    jan = _('Jan')
    feb = _('Feb')
    mar = _('Apr')
    apr = _('Apr')
    may = _('May')
    jun = _('Jun')
    jul = _('Jul')
    aug = _('Aug')
    sep = _('Sep')
    oct = _('Oct')
    nov = _('Nov')
    dec = _('Dec')

    month_numbers_convert = {
        1: jan,
        2: feb,
        3: mar,
        4: apr,
        5: may,
        6: jun,
        7: jul,
        8: aug,
        9: sep,
        10: oct,
        11: nov,
        12: dec
        }

    bananas_harvested = 0
    trees_planted = 0
    trees_harvested = 0
    predicted_per_month = {}
    harvested_per_month = {}
    predicted_harvest = 0
    yields = Reports_Yield.objects.filter(report_id__farm__id=farm_id);

    for single_yield in yields:
        if not month_numbers_convert[single_yield.report_id.month_numeric] in predicted_per_month:
            predicted_per_month[month_numbers_convert[single_yield.report_id.month_numeric]] = 0

        if not month_numbers_convert[single_yield.report_id.month_numeric] in harvested_per_month:
            harvested_per_month[month_numbers_convert[single_yield.report_id.month_numeric]] = 0

        predicted_per_month[month_numbers_convert[single_yield.report_id.month_numeric]] += single_yield.planted_amount_trees * 12
        harvested_per_month[month_numbers_convert[single_yield.report_id.month_numeric]] += single_yield.harvested_amount_kg_banana

    actual_vs_predicted = {}

    for i in range(1,13):
        actual_vs_predicted[month_numbers_convert[i]] = {}

        for y in range(0,2):
            actual_vs_predicted[month_numbers_convert[i]][y] = 0

    for month, predict in predicted_per_month.items():
        actual_vs_predicted[month][0] = predict

    for month, harvest in harvested_per_month.items():
        actual_vs_predicted[month][1] = harvest

    for report_yield in yields:
        bananas_harvested = bananas_harvested + report_yield.harvested_amount_kg_banana
        trees_planted = trees_planted + report_yield.planted_amount_trees
        trees_harvested = trees_harvested + report_yield.harvested_amount_trees

    #dict for the template
    context = {
        'language': language_code,
        'farm_id' : farm_id,
        'bananas_harvested': bananas_harvested,
        'trees_planted': trees_planted,
        'trees_harvested': trees_harvested,
        'actual_vs_predicted': actual_vs_predicted,
    }
    return render(request, 'farmer/overview/statistics.html', context)
