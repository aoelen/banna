from django.shortcuts import get_object_or_404, render, redirect

from farmer.models import Date, Farm, Report, Reports_Yield
from django.contrib.auth.models import User
from datetime import datetime, date
from time import strftime


#SHOW OVERVIEW REPORT
def overview_report(request, farm_id, year , month):
    list_trees_yield = []
    list_harvested_bananas_yield = []
    total_amount_trees = 0
    total_amount_harvested_kg = 0

    farm_object = Farm.objects.filter(id=farm_id)
    for farm in farm_object:
        reports = Report.objects.filter(farm=farm, month= month)

        for report in reports:
            fertilizer_used = report.fertilizer_used
            fertilizer_amount = report.fertilizer_amount

            yield_reports = Reports_Yield.objects.filter(report_id=report).order_by('id')
            for yield_number in yield_reports:

                total_amount_trees += yield_number.planted_amount_trees
                total_amount_harvested_kg += yield_number.harvested_amount_kg_banana

                list_trees_yield.append(
                    {
                    yield_number.yield_number: yield_number.planted_amount_trees
                    },
                )
                list_harvested_bananas_yield.append(
                    {
                    yield_number.yield_number: yield_number.harvested_amount_kg_banana
                    }
                )

    fertilizer = {
           'used': fertilizer_used,
            'amount': fertilizer_amount
        }

    trees = {
        'trees_yield': list_trees_yield,
        'trees_total': total_amount_trees

    }

    harvested = {
        'trees_yield': list_harvested_bananas_yield,
        'amount_total': total_amount_harvested_kg

    }

    date = {
        'month': month,
        'year': year
    }

    context = {
        'date': date,
        'trees': trees,
        'harvested': harvested,
        'fertilizer': fertilizer,
        'report' : report,
        'farm_id' : farm_id

    }

    return render(request, 'farmer/overview/reports.html', context)
