from django.shortcuts import get_object_or_404, render, redirect
from farmer.models import Report
from datetime import datetime, date
from django.utils import translation

def success(request, farm_id, year, month, report_id, language_code):
    user_language = language_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    Report.objects.filter(id=report_id).update(report_date=datetime.now().date())

    context = {
        'language':language_code,
        'report_id': report_id,
        'farm_id': farm_id,
        'year': year,
        'month': month,
    }

    return render(request, 'farmer/form/success.html', context)