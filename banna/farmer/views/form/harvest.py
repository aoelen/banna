from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import redirect
from farmer.models import Report, UserForm, Reports_Yield
from django.utils import translation


def form_harvest_trees(request, farm_id, year, month, report_id, language_code):
    print(language_code)
    user_language = language_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    message_alert = ""
    redirect_page = True

    if request.method == "POST":
        yields = request.POST.getlist('yield[]')
        for index, single_yield in enumerate(yields):
            if single_yield == "":
                message_alert = "#message_alert"
                redirect_page = False
                break
        if redirect_page == True:
            for index, single_yield in enumerate(yields):
                report = Report.objects.get(id=report_id)
                person, created = Reports_Yield.objects.update_or_create(
                    report_id=report, yield_number=index+1, defaults={"harvested_amount_trees": single_yield}
                )
            return redirect('/farmer/'+ str(language_code) + '/' + str(farm_id) + '/' + str(year) + '/' + str(month) + '/' + str(report_id) + "/harvestedbananasform/")

    reports_yield = Reports_Yield.objects.filter(report_id=report_id)

    yields = {}

    for report in reports_yield:
        yields[report.yield_number] = report.harvested_amount_trees

    context = {
        'language': language_code,
        'message_alert': message_alert,
        'yields': yields,
        'report_id': report_id,
        'farm_id': farm_id,
        'year': year,
        'month': month,
    }

    return render(request, 'farmer/form/harvest/trees.html', context)


def form_harvest_bananas(request, farm_id, year, month, report_id, language_code):
    print(language_code)
    user_language = language_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    message_alert = ""
    redirect_page = True

    if request.method == "POST":
        yields = request.POST.getlist('yield[]')
        for index, single_yield in enumerate(yields):
            if single_yield == "":
                message_alert = "#message_alert"
                redirect_page = False
                break

        if redirect_page == True:
            for index, single_yield in enumerate(yields):
                report = Report.objects.get(id=report_id)

                person, created = Reports_Yield.objects.update_or_create(
                    report_id=report, yield_number=index+1, defaults={"harvested_amount_kg_banana": single_yield}
                )
            return redirect('/farmer/' + str(language_code) + '/' + str(farm_id) + '/' + str(year) + '/' + str(month) + '/' + str(report_id) + "/fertilizerform/")

    reports_yield = Reports_Yield.objects.filter(report_id=report_id)

    yields = {}

    for report in reports_yield:
        yields[report.yield_number] = report.harvested_amount_kg_banana

    context = {
        'language': language_code,
        'message_alert': message_alert,
        'yields': yields,
        'report_id': report_id,
        'farm_id': farm_id,
        'year': year,
        'month': month,
    }

    return render(request, 'farmer/form/harvest/bananas.html', context)
