from django.shortcuts import get_object_or_404, render, redirect

from farmer.models import Date, Farm, Report, Reports_Yield
from django.contrib.auth.models import User
from datetime import datetime, date
from time import strptime
from django.utils import translation

#SHOW OVERVIEW MONTH REPORTS
def overview_months(request, farm_id, language_code):
    # If form is correct,post into database and return next page
    user_language = language_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]


    currentdate =  datetime.now().date()
    #Transform number into month name
    formated_month = datetime(int(currentdate.year), int(currentdate.month), int(currentdate.day))
    selected_month = formated_month.strftime("%B")

    farms = Farm.objects.filter(id=farm_id)
    for farm in farms:
        #Create of get new month report
        person, created = Report.objects.get_or_create(
            month = selected_month,
            month_numeric=int(currentdate.month),
            year = int(currentdate.year),
            farm = farm,
        )

    reports = Report.objects.filter(farm=farm_id)

    data = []
    for report in reports:
        month_name = report.month
        month_number = strptime(month_name, '%B').tm_mon

        #check if report is filled in
        if report.report_date is None:
            # user have enough time
            if currentdate <= datetime(report.year, month_number, 7).date():
                data.append({
                    'farm_id': farm_id,
                    'month': report.month,
                    'year': report.year,
                    'date':{
                        'message': " ",
                        'value': 'icons/angle-double-right.svg',
                    }
                })

            #warning for the user to fill in the form
            if currentdate > datetime(report.year, month_number, 7).date() and currentdate < datetime(report.year, month_number, 20).date():
                data.append({
                    'farm_id': farm_id,
                    'month': report.month,
                    'year': report.year,
                    'date':{
                        'message': 'error',
                        'value': 'icons/alert.png'
                    }
                })

            #alert user is to late
            if currentdate > datetime(report.year, month_number, 21).date():
                data.append({
                    'farm_id': farm_id,
                    'month': report.month,
                    'year': report.year,
                    'date':{
                        'message': 'danger',
                        'value': 'icons/cancel.png'
                    }
                })

        #user has filled the form correctly
        else:
            data.append({
                'farm_id': farm_id,
                'month': report.month,
                'year': report.year,
                'date': {
                    'message': "success",
                    'value': 'icons/check.png'
                }
            })

    #dict for the template
    context = {
        'data': data,
        'farm_id': farm_id,
        'language': language_code
    }

    return render(request, 'farmer/overview/months.html', context)
