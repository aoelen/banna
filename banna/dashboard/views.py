from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from farmer.models import Month, Farm, Report, UserForm, Reports_Yield


@login_required
def index(request):

    # Render the .html file
    return render(request, 'dashboard/dashboard.html')

def login(request):

    # Render the .html file
    return render(request, 'dashboard/login.html')

def dashboard(request):

    report_yields = Reports_Yield.objects.all()
    farms_amount = Farm.objects.count()

    total_bananas_harvested = 0
    total_trees_planted = 0

    for report_yield in report_yields:
        total_bananas_harvested = total_bananas_harvested + report_yield.harvested_amount_kg_banana
        total_trees_planted = total_trees_planted + report_yield.planted_amount_trees

    context = {
        'total_bananas_harvested': total_bananas_harvested,
        'total_trees_planted': total_trees_planted,
        'farms_amount': farms_amount
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

    trees = Reports_Yield.objects.all()
    farms = Farm.objects.all()

    data = []
    for farm in farms:
        data.append(
            {
                'farm name': farm.name,
                'farmer': farm.farmer.first_name,
                'pic': farm.person_in_charge.first_name,
                'zone': farm.zone
            }
        )
        print(data)

        reports = Report.objects.filter(farm_id = farm)

        for report in report:
            yields = Reports_Yield.objects.filter(report_id = report)



    count = 0
    context = {
        'trees': trees

    }
    print(context)

    # Render the .html file
    return render(request, 'dashboard/trees.html', context)

def users(request):

    # Render the .html file
    return render(request, 'dashboard/users.html')
