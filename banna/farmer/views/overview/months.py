from django.shortcuts import get_object_or_404, render, redirect

from farmer.models import Date, Farm, Report, Reports_Yield
from django.contrib.auth.models import User
from datetime import datetime, date
from time import strptime


#SHOW OVERVIEW MONTH REPORTS
def overview_months(request, farm_id):
    currentdate =  datetime.now().date()

    #Transform number into month name
    formated_month = datetime(int(currentdate.year), int(currentdate.month), int(currentdate.day))
    selected_month = formated_month.strftime("%B")

    #Create of get new month report
    person, created = Report.objects.get_or_create(
         month=selected_month, year=currentdate.year, farm_id=farm_id, month_numeric=currentdate.month
    )

    reports = Report.objects.filter(farm=farm_id)

    for report in reports:
        month_name = report.month
        month_number = strptime(month_name, '%B').tm_mon

        data = {}
        data['report'] = {
            'farm_id': farm_id,
            'month': report.month,
            'year': report.year
            }

        if currentdate <= datetime(report.year, month_number, 7).date():
            data['date'] = {
                'value': 'test'
            }
        if currentdate > datetime(report.year, month_number, 7).date() and currentdate < datetime(report.year, month_number, 20).date():
            data['date'] = {
                'value': 'test'
            }

        if currentdate > datetime(report.year, month_number, 21).date():
            data['date'] = {
                'value': 'test'
            }
        print(data)

    context = {
        'reports': reports,
        'farm_id': farm_id
    }

    return render(request, 'farmer/overview/months.html', context)
