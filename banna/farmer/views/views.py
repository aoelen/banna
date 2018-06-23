from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from farmer.models import Month, Farm, Report

def index(request):
    return HttpResponse("<h2>You are at the farmer page!</h2>")

def overview(request):

    context = {

    }

    return render(request, 'farmer/overview.html', context)

def select_month(request, farm_id, year, month):
    farm_object = Farm.objects.filter(id=farm_id)
    for farm in farm_object:
        reports = Report.objects.filter(farm=farm)
        for i in reports:
            print (i.farm)

    print(year)
    print(month)
    context = {

    }

    return render(request, 'farmer/select_month.html', context)

def form_planted(request):

    context = {

    }

    return render(request, 'farmer/form_planted.html', context)


def form_harvest(request):

    context = {

    }

    return render(request, 'farmer/form_harvest.html', context)


def form_fertilizer(request):

    context = {

    }

    return render(request, 'farmer/form_fertilizer.html', context)


def login(request):

    context = {

    }

    return render(request, 'farmer/login.html', context)
