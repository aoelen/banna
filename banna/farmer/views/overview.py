from django.shortcuts import get_object_or_404, render, redirect

from farmer.models import Month, Farm, Report, Reports_Yield
from django.contrib.auth.models import User
import datetime


#SHOW OVERVIEW FARMS
def overview_farm(request):
    for loggedin_user in  User.objects.filter(id= request.user.id):
        farms = Farm.objects.filter(person_in_charge=loggedin_user)
    return render(request, 'farmer/farms.html', {'farms': farms})


#SHOW OVERVIEW MONTH REPORTS
def overview_months(request, farm_id):
    user = User.objects.filter(id=request.user.id)

    reports = Report.objects.filter(farm=farm_id)
    return render(request, 'farmer/overview.html', {
        'reports': reports
    })


#SHOW OVERVIEW REPORT
def overview_report(request, farm_id, year, month_id , month):
    list_planted_trees_yield = []
    list_harvested_bananas_yield = []
    total_amount_planted_trees = 0
    total_amount_harvested_kg = 0

    farm_object = Farm.objects.filter(id=farm_id)
    for farm in farm_object:
        reports = Report.objects.filter(farm=farm, month_id= month_id)

        for report in reports:
            fertilizer_used = report.fertilizer_used
            fertilizer_amount = report.fertilizer_amount

            yield_reports = Reports_Yield.objects.filter(report_id=report).order_by('id')
            for yield_number in yield_reports:

                total_amount_planted_trees += yield_number.planted_amount_trees
                total_amount_harvested_kg += yield_number.harvested_amount_kg_banana

                list_planted_trees_yield.append(
                    {
                    yield_number.yield_number: yield_number.planted_amount_trees
                    },
                )
                list_harvested_bananas_yield.append(
                    {
                    yield_number.yield_number: yield_number.harvested_amount_kg_banana
                    }
                )
    print(report)

    fertilizer = {
           'used': fertilizer_used,
            'amount': fertilizer_amount
        }

    planted = {
        'trees_yield': list_planted_trees_yield,
        'trees_total': total_amount_planted_trees

    }

    harvested = {
        'trees_yield': list_harvested_bananas_yield,
        'amount_total': total_amount_harvested_kg

    }

    date = {
        'month_id': month_id,
        'month': month,
        'year': year
    }

    context = {
        'date': date,
        'planted': planted,
        'harvested': harvested,
        'fertilizer': fertilizer,
        'report' : report,
        'farm_id' : farm_id

    }

    return render(request, 'farmer/select_month.html', context)
