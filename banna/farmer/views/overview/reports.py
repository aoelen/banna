from django.shortcuts import get_object_or_404, render, redirect

from farmer.models import Date, Farm, Report, Reports_Yield
from django.contrib.auth.models import User
from datetime import datetime, date
from time import strftime
from django.contrib.auth.decorators import user_passes_test
from farmer.views import auth_check
import pprint

#SHOW OVERVIEW REPORT
def overview_report(request, farm_id, year , month):
    data = {}
    total_amount_planted_trees = 0
    total_amount_harvested_trees = 0
    total_amount_harvested_kg = 0

    farm_object = Farm.objects.filter(id=farm_id)
    for farm in farm_object:
        reports = Report.objects.filter(farm=farm, month= month)

        for report in reports:
            data['fertilizer'] = {
                'used': report.fertilizer_used,
                'amount': report.fertilizer_amount
            }

            yield_reports = Reports_Yield.objects.filter(report_id=report).order_by('id')
            for yield_number in yield_reports:
                print(yield_number)
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

    data['date'] = {
        'month': month,
        'year': year
    }

    context = {
        'data': data,
        'report' : report,
        'farm_id' : farm_id

    }
    return render(request, 'farmer/overview/reports.html', context)



