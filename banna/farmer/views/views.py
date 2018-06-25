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


def form_planted(request, report_id):
    if request.method == "POST":

        yields = request.POST.getlist('yield[]')

        for index, single_yield in enumerate(yields):
            report = Report.objects.get(id=report_id)

            person, created = Reports_Yield.objects.update_or_create(
                report_id=report, yield_number=index+1, defaults={"planted_amount_trees": single_yield}
            )

        return redirect('/farmer/form_harvest/' + str(report_id))


    reports_yield = Reports_Yield.objects.filter(report_id=report_id)

    yields = {}

    for report in reports_yield:
        yields[report.yield_number] = report.amount_trees

    context = {
        'yields': yields,
        'report_id': report_id
    }

    return render(request, 'farmer/form_planted.html', context)


def form_harvest(request, report_id):
    if request.method == "POST":

        yields = request.POST.getlist('yield[]')

        for index, single_yield in enumerate(yields):
            report = Report.objects.get(id=report_id)

            person, created = Reports_Yield.objects.update_or_create(
                report_id=report, yield_number=index+1, defaults={"harvested_amount_kg_banana": single_yield}
            )

        return redirect('/farmer/form_fertilizer/' + str(report_id))

    reports_yield = Reports_Yield.objects.filter(report_id=report_id)

    yields = {}

    for report in reports_yield:
        yields[report.yield_number] = report.harvested_amount_kg_banana

    context = {
        'yields': yields,
        'report_id': report_id
    }

    return render(request, 'farmer/form_harvest.html', context)


def form_fertilizer(request, report_id):
    if request.method == "POST":
        Report.objects.filter(id=report_id).update(fertilizer_amount=request.POST.get('fertilizer_kgs', ''), fertilizer_used=request.POST.get('fertilizer_used', ''))

        return redirect('/farmer/success/' + str(report_id))

    report = Report.objects.get(id=report_id)

    context = {
        'report': report,
        'report_id': report_id
    }

    return render(request, 'farmer/form_fertilizer.html', context)

def success(request, report_id):
    return render(request, 'farmer/success.html')

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
