from django.shortcuts import get_object_or_404, render, redirect

from farmer.models import Date, Farm, Report, Reports_Yield
from django.contrib.auth.models import User
from datetime import datetime, date
from time import strptime
import pprint

#SHOW OVERVIEW MONTH REPORTS
def overview_months(request, farm_id):
    currentdate =  datetime.now().date()
    #Transform number into month name
    formated_month = datetime(int(currentdate.year), int(currentdate.month), int(currentdate.day))
    selected_month = formated_month.strftime("%B")

    farms = Farm.objects.filter(id=farm_id)
    for farm in farms:
        print(farm.id)
        #Create of get new month report
        person, created = Report.objects.get_or_create(
            month = selected_month,
            month_numeric=int(currentdate.month),
            year = int(currentdate.year),
            farm = farm,
        )

    reports = Report.objects.filter(farm=farm_id)

    data = {}
    for report in reports:
        month_name = report.month
        month_number = strptime(month_name, '%B').tm_mon
        data['report'] = {
            'farm_id': farm_id,
            'month': report.month,
            'year': report.year
        }

        if report.report_date is None:
            if currentdate <= datetime(report.year, month_number, 7).date():
                data['report']['date'] = {
                    'message': " ",
                    'value': 'fas fa-angle-double-right'
                }
            if currentdate > datetime(report.year, month_number, 7).date() and currentdate < datetime(report.year, month_number, 20).date():
                data['report']['date'] = {
                    'message': 'error',
                    'value': 'fas fa-exclamation-triangle'
                }

            if currentdate > datetime(report.year, month_number, 21).date():
                data['report']['date'] = {
                    'message': 'danger',
                    'value': 'fas fa-exclamation-circle'
                }
        else:
            data['report']['date'] = {
                'message': "success",
                'value': 'fas fa-check-circle'
            }
    print(data)

    context = {
        'data': data,
        'farm_id': farm_id
    }

    return render(request, 'farmer/overview/months.html', context)
