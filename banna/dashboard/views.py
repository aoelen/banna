from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from farmer.models import Farm, Report, UserForm, Reports_Yield

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

    # Render the .html file
    return render(request, 'dashboard/factory_overview.html')

def factory(request):

    # Render the .html file
    return render(request, 'dashboard/factory.html')

def farmers(request):

    # Render the .html file
    return render(request, 'dashboard/farmers.html')

def harvests(request):

    # Render the .html file
    return render(request, 'dashboard/harvests.html')

def trees(request):

    # Render the .html file
    return render(request, 'dashboard/trees.html')

def users(request):

    # Render the .html file
    return render(request, 'dashboard/users.html')
