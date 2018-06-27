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

    ## Trees per yield per month
    yields_trees = Reports_Yield.objects.filter(report_id__year="2018").select_related('report_id').order_by('report_id__month_numeric', '-id');

    trees_yield_month = {}

    for i in range(1,13):
        trees_yield_month[i] = {}

        for y in range(1,6):
            trees_yield_month[i][y] = 0

    for yields_tree in yields_trees:
        yields_tree.yield_number = int(yields_tree.yield_number.replace('Yield ', ''))
        if not yields_tree.report_id.month_numeric in trees_yield_month:
            trees_yield_month[yields_tree.report_id.month_numeric] = {}

        if not yields_tree.yield_number in trees_yield_month[yields_tree.report_id.month_numeric]:
            trees_yield_month[yields_tree.report_id.month_numeric][yields_tree.yield_number] = 0;

        trees_yield_month[yields_tree.report_id.month_numeric][yields_tree.yield_number] = trees_yield_month[yields_tree.report_id.month_numeric][yields_tree.yield_number] + yields_tree.planted_amount_trees

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
        'farmers_no_update': farmers_no_update,
        'trees_yield_month': trees_yield_month
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

    harvests = Reports_Yield.objects.select_related('report_id__farm__farmer').order_by('-report_id__year', '-report_id__month', '-id');

    harvest_per_month = {}

    for harvest in harvests:
        if not harvest.report_id.month in harvest_per_month:
            harvest_per_month[harvest.report_id.month] = 0

        harvest_per_month[harvest.report_id.month] = harvest_per_month[harvest.report_id.month] + harvest.harvested_amount_kg_banana

    context = {
        'harvests': harvests,
        'harvest_per_month': harvest_per_month
    }

    # Render the .html file
    return render(request, 'dashboard/harvests.html', context)

def trees(request):
    yields = Reports_Yield.objects.select_related('report_id__farm__farmer').order_by('-report_id__year', '-report_id__month', '-id'); #.filter(report_id__year="2018").

    planted_per_month = {}

    for row in yields:
        if not row.report_id.month in planted_per_month:
            planted_per_month[row.report_id.month] = 0

        planted_per_month[row.report_id.month] = planted_per_month[row.report_id.month] + row.planted_amount_trees


    context = {
        'rows': yields,
        'planted_per_month': planted_per_month
    }

    # Render the .html file
    return render(request, 'dashboard/trees.html', context)

def users(request):

    # Render the .html file
    return render(request, 'dashboard/users.html')
