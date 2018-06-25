from django.shortcuts import get_object_or_404, render, redirect

from farmer.models import Month, Farm, Report, Reports_Yield
from django.contrib.auth.models import User


#SHOW OVERVIEW FARMS
def overview_farm(request):
    for loggedin_user in  User.objects.filter(id= request.user.id):
        farms = Farm.objects.filter(person_in_charge=loggedin_user)
    return render(request, 'farmer/farms.html', {'farms': farms})


#SHOW OVERVIEW MONTH REPORTS
def overview_months(request, farm_id):
    reports = Report.objects.filter(farm=farm_id)
    return render(request, 'farmer/overview.html', {'reports': reports})


#SHOW OVERVIEW REPORT
def overview_report(request, farm_id, year, month_id , month):
    planted_trees = []
    harvested_bananas = []
    total_amount_planted_trees = 0
    total_amount_harvested_kg = 0

    farm_object = Farm.objects.filter(id=farm_id)
    for farm in farm_object:
        reports = Report.objects.filter(farm=farm, month_id= month_id)
        for report in reports:
            yield_reports = Reports_Yield.objects.filter(report_id=report).order_by('id')
            for yield_number in yield_reports:
                fertilizer_used = report.fertilizer_used
                fertilizer_amount = report.fertilizer_amount

                total_amount_planted_trees += yield_number.planted_amount_trees
                total_amount_harvested_kg += yield_number.harvested_amount_kg_banana

                planted_trees.append(
                    {
                    yield_number.yield_number: yield_number.planted_amount_trees
                    },
                )
                harvested_bananas.append(
                    {
                    yield_number.yield_number: yield_number.harvested_amount_kg_banana
                    }
                )

    context = {
        'month' : month,
        'month_id' : month_id,
        'year' : year,
        'planted_trees': planted_trees,
        'harvested_bananas': harvested_bananas,
        'fertilizer_used': fertilizer_used,
        'fertilizer_amount': fertilizer_amount,
        'farm' : farm_id

    }

    return render(request, 'farmer/select_month.html', context)