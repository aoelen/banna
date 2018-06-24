from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponse
from farmer.models import Month, Farm, Report, UserForm, Reports_Yield

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

def form_planted(request, report_id):
    if request.method == "POST":

        return redirect('/farmer/form_harvest/' + str(report_id))


    reports_yield = Reports_Yield.objects.filter(report_id=report_id)

    yields = {}

    for report in reports_yield:
        yields[report.yield_number] = report.planted_amount_trees

    context = {
        'yields': yields,
        'report_id': report_id
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
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            login_item = form.save(commit=False)
            login_item.save()
            return redirect('/farmer/overview/')
    else:
        form = UserForm()
    return render(request, 'farmer/login.html', {'login': form})

    context = {

    }

    return render(request, 'farmer/login.html', context)
