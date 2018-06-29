from django.shortcuts import get_object_or_404, render, redirect
from farmer.models import Date, Farm, Report, Reports_Yield
from django.contrib.auth.models import User
from datetime import datetime, date
from time import strftime
from django.contrib.auth.decorators import user_passes_test
from farmer.views import auth_check

month_numbers_convert = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}

def statistics(request, farm_id):

    bananas_harvested = 0
    trees_planted = 0
    trees_harvested = 0
    predicted_per_month = {}
    harvested_per_month = {}
    predicted_harvest = 0
    yields = Reports_Yield.objects.filter(report_id__farm__id=farm_id);
    # print(yields)

    for single_yield in yields:
        if not month_numbers_convert[single_yield.report_id.month_numeric] in predicted_per_month:
            predicted_per_month[month_numbers_convert[single_yield.report_id.month_numeric]] = 0

        if not month_numbers_convert[single_yield.report_id.month_numeric] in harvested_per_month:
            harvested_per_month[month_numbers_convert[single_yield.report_id.month_numeric]] = 0

        predicted_per_month[month_numbers_convert[single_yield.report_id.month_numeric]] += single_yield.planted_amount_trees * 12
        harvested_per_month[month_numbers_convert[single_yield.report_id.month_numeric]] += single_yield.harvested_amount_kg_banana

    # print(predicted_per_month)
    # print(harvested_per_month)

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


    context = {
        'farm_id' : farm_id,
        'bananas_harvested': bananas_harvested,
        'trees_planted': trees_planted,
        'trees_harvested': trees_harvested,
        'actual_vs_predicted': actual_vs_predicted,
    }
    return render(request, 'farmer/overview/statistics.html', context)
