from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from farmer.models import Farm, Report, UserForm, Reports_Yield
import pprint
import datetime


@login_required
def index(request):

    # Render the .html file
    return render(request, 'dashboard/dashboard.html')

def login(request):

    # Render the .html file
    return render(request, 'dashboard/login.html')

def dashboard(request):
    now = datetime.datetime.now()
    report_yields = Reports_Yield.objects.all()
    farms_amount = Farm.objects.count()
    reports_this_year = Report.objects.filter(year=now.year).order_by('month_numeric');

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

    yields = Reports_Yield.objects.filter(report_id__year="2018");

    harvest_per_month = {}
    planted_per_month = {}

    for single_yield in yields:
        if not 'single_yield.report_id.month_numeric' in harvest_per_month:
            harvest_per_month[month_numbers_convert[single_yield.report_id.month_numeric]] = 0
            planted_per_month[month_numbers_convert[single_yield.report_id.month_numeric]] = 0

        harvest_per_month[month_numbers_convert[single_yield.report_id.month_numeric]] = single_yield.harvested_amount_kg_banana
        planted_per_month[month_numbers_convert[single_yield.report_id.month_numeric]] = single_yield.planted_amount_trees

    total_bananas_harvested = 0
    total_trees_planted = 0

    for report_yield in report_yields:
        total_bananas_harvested = total_bananas_harvested + report_yield.harvested_amount_kg_banana
        total_trees_planted = total_trees_planted + report_yield.planted_amount_trees

    ## Farmer monthly updates
    all_farms = Farm.objects.all()

    farmers_update = 0
    farmers_no_update = 0
    for farm in all_farms:
        report = Report.objects.filter(farm_id=farm, month_numeric=now.month).count()

        if report == 0:
            farmers_no_update = farmers_no_update + 1
        else:
            farmers_update = farmers_update + 1

    context = {
        'total_bananas_harvested': total_bananas_harvested,
        'total_trees_planted': total_trees_planted,
        'farms_amount': farms_amount,
        'harvest_per_month': harvest_per_month,
        'planted_per_month': planted_per_month,
        'current_month': month_numbers_convert[now.month],
        'farmers_update': farmers_update,
        'farmers_no_update': farmers_no_update
    }

    # Render the .html file
    return render(request, 'dashboard/dashboard.html', context)

def add_farmer(request):

    # Render the .html file
    return render(request, 'dashboard/add_farmer.html')

def add_user(request):

    # Render the .html file
    return render(request, 'dashboard/add_user.html')

def edit_farmer(request):

    # Render the .html file
    return render(request, 'dashboard/edit_farmer.html')

def factory_data(request):

    # Render the .html file
    return render(request, 'dashboard/factory_data.html')

def factory_overview(request):

    factory_input = Farm.objects.all()


    context = {
        'factory_input': factory_input
    }
    print(context)

    # Render the .html file
    return render(request, 'dashboard/factory_overview.html', context)

def factory(request):

    # Render the .html file
    return render(request, 'dashboard/factory.html')

def farmers(request):
    farmers = Farm.objects.all()

    context = {
        'farmers': farmers
    }
    print(context)
    # Render the .html file
    return render(request, 'dashboard/farmers.html', context)

def harvests(request):

    harvests = Reports_Yield.objects.all()
    count = 0
    context = {
        'harvests': harvests

    }
    print(context)

    # Render the .html file
    return render(request, 'dashboard/harvests.html', context)

def trees(request):

    # trees = Reports_Yield.objects.all()
    # farms = Farm.objects.all()
    # list_farm_ids=[]
    # for farm in farms:
    #     reports = Report.objects.filter(farm_id = farm)
    #     for report in reports:
    #         farm_id = report.farm
    #         if farm_id not in list_farm_ids:
    #             list_farm_ids.append(farm)
    #
    # data = {}
    # # print(list_farm_ids)
    # for farm in list_farm_ids:
    #     data['username'] = {
    #                 'farm name': farm.name,
    #                 'farmer': farm.farmer.first_name,
    #                 # 'pic': farm.person_in_charge.first_name,
    #                 'zone': farm.zone,
    #             }
    #
    #     reports = Report.objects.filter(farm_id = farm)
    #     for report in reports:
    #         data['username']['report'] = {
    #                     'id':report.id,
    #                     'fertilizer':{
    #                         'used':report.fertilizer_used,
    #                         'amount': report.fertilizer_amount
    #                     },
    #                     'month':report.month,
    #                     'year':report.year,
    #                 }
    #         data['username']['report']['yields'] ={}
    #         yields = Reports_Yield.objects.filter(report_id = report)
    #         for yield_id in yields:
    #             data['username']['report'] ['yields'] = {
    #                         'yield': yield_id.yield_number,
    #                         'harvested_amount_kg_banana': yield_id.harvested_amount_kg_banana,
    #                         'planted_amount_trees': yield_id.planted_amount_trees
    #                     }
    #             print(yield_id.yield_number)
    #             print(yield_id.harvested_amount_kg_banana)
    #             print(yield_id.planted_amount_trees)
    #
    # pprint.pprint(data)
    #
    #
    #
    #
    # count = 0
    # context = {
    #     'trees': data
    #
    # }

    # Render the .html file
    return render(request, 'dashboard/trees.html')

def users(request):

    # Render the .html file
    return render(request, 'dashboard/users.html')
