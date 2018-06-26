from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import redirect
from farmer.models import Report, UserForm, Reports_Yield, Date, Farm
from django.contrib.auth.models import User
from time import strftime

def form_planted(request, farm_id, year, month, report_id):
    if request.method == "POST":

        yields = request.POST.getlist('yield[]')

        for index, single_yield in enumerate(yields):
            report = Report.objects.get(id=report_id)

            person, created = Reports_Yield.objects.update_or_create(
                report_id=report, yield_number=index+1, defaults={"planted_amount_trees": single_yield}
            )

        return redirect('/farmer/'+ str(farm_id) + '/' + str(year) + '/' + str(month) + '/' + str(report_id) + "/harvestedtreesform/")

    reports_yield = Reports_Yield.objects.filter(report_id=report_id)

    yields = {}

    for report in reports_yield:
        yields[report.yield_number] = report.planted_amount_trees

    context = {
        'yields': yields,
        'report_id': report_id,
        'farm_id': farm_id,
        'year': year,
        'month': month,
    }

    return render(request, 'farmer/form/planted.html', context)