from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from django.http import HttpResponse
from farmer.models import Month, Farm, Report, UserForm, Yield, Tree

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
        for report in reports:
            print (report.farm)
            print (report.fertilizer_used)
            print (report.fertilizer_amount)
            print (report.yields_id)

            for yield_number in Yield.objects.filter(report=farm):
                trees_report = Tree.objects.filter(farm = farm, yield_id = yield_number)
                print()
                for tree_ in trees_report:
                    print(tree_.planted_amount_trees)


    context = {
        'month' : month,
        'year' : year,
        'report': report,
        # 'tree': trees_report
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
