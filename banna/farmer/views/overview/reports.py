from django.shortcuts import get_object_or_404, render, redirect

from farmer.models import Date, Farm, Report, Reports_Yield
from django.contrib.auth.models import User
from datetime import datetime, date
from time import strftime
from django.contrib.auth.decorators import user_passes_test
from farmer.views import auth_check
from django.utils import translation

#SHOW OVERVIEW REPORT
def overview_report(request, farm_id, year , month, language_code):
    # If form is correct,post into database and return next page
    user_language = language_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    data = {}
    total_amount_planted_trees = 0
    total_amount_harvested_trees = 0
    total_amount_harvested_kg = 0

    #get data of the month report
    farm_object = Farm.objects.filter(id=farm_id)
    for farm in farm_object:
        reports = Report.objects.filter(farm_id=farm, month= month)

        for report in reports:
            data['fertilizer'] = {
                'used': report.fertilizer_used,
                'amount': report.fertilizer_amount
            }

            yield_reports = Reports_Yield.objects.filter(report_id=report).order_by('id')
            for yield_number in yield_reports:
                total_amount_planted_trees += yield_number.planted_amount_trees
                total_amount_harvested_trees += yield_number.harvested_amount_trees
                total_amount_harvested_kg += yield_number.harvested_amount_kg_banana

                data.setdefault('trees', []).append({
                    'planted': {
                        yield_number.yield_number:yield_number.planted_amount_trees,
                    },
                    'harvested': {
                        yield_number.yield_number: yield_number.harvested_amount_trees,
                    },
                    'bananas': {
                        yield_number.yield_number: yield_number.harvested_amount_kg_banana,
                    },
                })


        data['total_planted'] = total_amount_planted_trees
        data['total_harvested'] = total_amount_harvested_trees
        data['total_bananas_kg'] = total_amount_harvested_kg

    #get the month and year of the report
    data['date'] = {
        'month': month,
        'year': year
    }

    #dict for the template
    context = {
        'data': data,
        'report' : report,
        'farm_id' : farm_id,
        'language': language_code

    }
    return render(request, 'farmer/overview/reports.html', context)



