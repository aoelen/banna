from django.shortcuts import get_object_or_404, render, redirect
from django.shortcuts import redirect
from farmer.models import Report, UserForm, Reports_Yield



def form_fertilizer(request, farm_id, year, month, report_id):
    message_alert = ""
    if request.method == "POST":

        report_input = request.POST.get('fertilizer_used', '')

        if report_input == 'Yes' or report_input == 'No':
            if request.POST.get('fertilizer_kgs', '') is not '':
                fertilizer_amount = request.POST.get('fertilizer_kgs', '')
            else:
                fertilizer_amount = None


            Report.objects.filter(id=report_id).update(fertilizer_amount=fertilizer_amount,
                                                        fertilizer_used=request.POST.get('fertilizer_used', ''),
                                                        )

            return redirect('/farmer/'+ str(farm_id) + '/' + str(year) + '/' + str(month) + '/' + str(report_id) + "/succes/")
        else:
            message_alert = "#message_alert"

    report = Report.objects.get(id=report_id)


    context = {
        'message_alert': message_alert,
        'report': report,
        'report_id': report_id,
        'farm_id': farm_id,
        'year': year,
        'month': month,
    }

    return render(request, 'farmer/form/fertilizer.html', context)

