from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from farmer.models import Farm, Report, UserForm, Reports_Yield, Factory_Data
import pprint
import datetime
from django.utils import translation

month_numbers_convert = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sep',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}

@login_required
def index(request):
    # Render the .html file
    return render(request, 'dashboard/dashboard.html')

def login(request):

    # Render the .html file
    return render(request, 'dashboard/login.html')

def dashboard(request):
    if not request.session['language_code']:
        language_code = request.session['language_code']
    if request.session['language_code'] == 'en':
        language_code = 'en'
    if request.session['language_code'] == 'ms':
        language_code = 'ms'

    if request.method == "POST":
        language_en = request.POST.get('english', '')
        language_ms = request.POST.get('malay', '')
        if not language_en:
            language_code = language_ms
        else:
            language_code = language_en

    user_language = language_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]


    request.session['language_code'] = language_code

    now = datetime.datetime.now()
    report_yields = Reports_Yield.objects.all()
    farms_amount = Farm.objects.count()
    reports_this_year = Report.objects.filter(year=now.year).order_by('month_numeric')
    yields = Reports_Yield.objects.filter(report_id__year="2018")

    harvest_per_month = {}
    planted_per_month = {}

    for single_yield in yields:
        if not month_numbers_convert[single_yield.report_id.month_numeric] in harvest_per_month:
            harvest_per_month[month_numbers_convert[single_yield.report_id.month_numeric]] = 0

        if not month_numbers_convert[single_yield.report_id.month_numeric] in planted_per_month:
            planted_per_month[month_numbers_convert[single_yield.report_id.month_numeric]] = 0

        harvest_per_month[month_numbers_convert[single_yield.report_id.month_numeric]] += single_yield.harvested_amount_kg_banana
        planted_per_month[month_numbers_convert[single_yield.report_id.month_numeric]] += single_yield.planted_amount_trees

    total_bananas_harvested = 0
    total_trees_planted = 0

    for report_yield in report_yields:
        total_bananas_harvested = total_bananas_harvested + report_yield.harvested_amount_kg_banana
        total_trees_planted = total_trees_planted + report_yield.planted_amount_trees

    ## Total KGs harvested
    factory_datas = Factory_Data.objects.all()

    total_factory_kgs = 0
    for factory_data in factory_datas:
        total_factory_kgs = total_factory_kgs + factory_data.kgs_received

    ## KGS harvested vs KGs received
    harvest_vs_received = {}
    factory_year_datas = Factory_Data.objects.filter(year=now.year)

    for i in range(1,13):
        harvest_vs_received[month_numbers_convert[i]] = {}

        for y in range(0,2):
            harvest_vs_received[month_numbers_convert[i]][y] = 0

    for month, harvest in harvest_per_month.items():
        harvest_vs_received[month][0] = harvest

    for factory_year_data in factory_year_datas:
        harvest_vs_received[month_numbers_convert[factory_year_data.month]][1] = factory_year_data.kgs_received

    ## Trees per yield per month
    yields_trees = Reports_Yield.objects.filter(report_id__year="2018").select_related('report_id').order_by('report_id__month_numeric', '-id');

    trees_yield_month = {}

    for i in range(1,13):
        trees_yield_month[i] = {}

        for y in range(1,6):
            trees_yield_month[i][y] = 0

    for yields_tree in yields_trees:
        yields_tree.yield_number = int(yields_tree.yield_number.replace('Yield ', ''))
        if not yields_tree.report_id.month_numeric in trees_yield_month:
            trees_yield_month[yields_tree.report_id.month_numeric] = {}

        if not yields_tree.yield_number in trees_yield_month[yields_tree.report_id.month_numeric]:
            trees_yield_month[yields_tree.report_id.month_numeric][yields_tree.yield_number] = 0;

        trees_yield_month[yields_tree.report_id.month_numeric][yields_tree.yield_number] = trees_yield_month[yields_tree.report_id.month_numeric][yields_tree.yield_number] + yields_tree.planted_amount_trees

    trees_yield_month_converted = {}

    # convert month numbers to year
    for i in range(1,13):
        trees_yield_month_converted[month_numbers_convert[i]] = trees_yield_month[i]

    ## Farmer monthly updates
    all_farms = Farm.objects.select_related('farmer').all()

    farmers_update = 0
    farmers_no_update = 0

    farmer_updates_list = []
    #i = 0
    for farm in all_farms:
        #if not i in farmer_updates_list:
        #    farmer_updates_list[i] = {}

        report = Report.objects.filter(farm_id=farm, month_numeric=now.month-1)
        #user = User.objects.filter()
        report_count = report.count()

        item = {
            'name': farm.farmer.first_name + ' ' + farm.farmer.last_name,
            'completed': report_count == 1
        }

        farmer_updates_list.append(item)

        #farmer_updates_list[i]['name'] = farm.farmer.first_name + ' ' + farm.farmer.last_name
        #farmer_updates_list[i]['completed'] = report_count == 1

        if report_count == 0:
            farmers_no_update = farmers_no_update + 1
        else:
            farmers_update = farmers_update + 1

        i = i+1


    farms = Farm.objects.all()

    context = {
        'total_bananas_harvested': total_bananas_harvested,
        'total_trees_planted': total_trees_planted,
        'farms_amount': farms_amount,
        'harvest_per_month': harvest_per_month,
        'planted_per_month': planted_per_month,
        'current_month': month_numbers_convert[now.month],
        'last_month': month_numbers_convert[now.month-1],
        'farmers_update': farmers_update,
        'farmers_no_update': farmers_no_update,
        'trees_yield_month': trees_yield_month_converted,
        'total_factory_kgs': total_factory_kgs,
        'harvest_vs_received': harvest_vs_received,
        'farms': farms,
        'farmer_updates_list': farmer_updates_list
    }

    # Render the .html file
    return render(request, 'dashboard/dashboard.html', context)

def add_farmer(request):

    # Render the .html file
    return render(request, 'dashboard/add_farmer.html')

def add_user(request):

    # Render the .html file
    return render(request, 'dashboard/add_user.html')

def edit_farmer(request):

    # Render the .html file
    return render(request, 'dashboard/edit_farmer.html')

def factory_data(request):
    language_code = request.session['language_code']

    if request.method == "POST":
        language_en = request.POST.get('english', '')
        language_ms = request.POST.get('malay', '')
        if not language_en:
            language_code = language_ms
        else:
            language_code = language_en
    user_language = language_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    request.session['language_code'] = language_code
    now = datetime.datetime.now()

    if request.method == "POST":
        month = request.POST.get('month', '')
        kgs_received = request.POST.get('kgs_received', '')

        Factory_Data.objects.update_or_create(
            month=month, kgs_received=kgs_received, year=now.year
        )

        return redirect('/dashboard/factory')

    factory_datas = Factory_Data.objects.filter(year=now.year)

    months_filledin = []

    for factory_data in factory_datas:
        months_filledin.append(factory_data.month)

    context = {
        'months': month_numbers_convert,
        'months_filledin': months_filledin
    }

    # Render the .html file
    return render(request, 'dashboard/factory_data.html', context)

def factory_data_delete(request, data_id):
    Factory_Data.objects.filter(id=data_id).delete()

    return redirect('/dashboard/factory')


def factory_data_edit(request, data_id):
    language_code = request.session['language_code']

    if request.method == "POST":
        language_en = request.POST.get('english', '')
        language_ms = request.POST.get('malay', '')
        if not language_en:
            language_code = language_ms
        else:
            language_code = language_en
    user_language = language_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    request.session['language_code'] = language_code


    if request.method == "POST":
        kgs_received = request.POST.get('kgs_received', '')

        Factory_Data.objects.filter(id=data_id).update(
            kgs_received=kgs_received
        )

        return redirect('/dashboard/factory')

    data = Factory_Data.objects.get(id=data_id)

    context = {
        'data': data,
        'month': month_numbers_convert
    }

    return render(request, 'dashboard/factory_data_edit.html', context)


    #return redirect('/dashboard/factory_data_edit', context)


def factory_overview(request):
    language_code = request.session['language_code']

    if request.method == "POST":
        language_en = request.POST.get('english', '')
        language_ms = request.POST.get('malay', '')
        if not language_en:
            language_code = language_ms
        else:
            language_code = language_en
    user_language = language_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    request.session['language_code'] = language_code

    now = datetime.datetime.now()

    factory_datas = Factory_Data.objects.filter(year=now.year).order_by('id')
    yields = Reports_Yield.objects.filter(report_id__year="2018")

    harvest_per_month = {}

    for single_yield in yields:
        if not single_yield.report_id.month_numeric in harvest_per_month:
            harvest_per_month[single_yield.report_id.month_numeric] = 0

        harvest_per_month[single_yield.report_id.month_numeric] += single_yield.harvested_amount_kg_banana

    graph_datas = {}

    for factory_data in factory_datas:
        graph_datas[factory_data.month] = factory_data.kgs_received

    graph_datas_converted = {}
    for i in range(1,13):
        if i in graph_datas:
            received = graph_datas[i]
        else:
            received = 0

        if i in harvest_per_month:
            kgs = harvest_per_month[i]
        else:
            kgs = 0

        graph_datas_converted[month_numbers_convert[i]] = {
            'received': received,
            'kgs': kgs
        }

    context = {
        'factory_datas': factory_datas,
        'graph_datas': graph_datas_converted
    }

    # Render the .html file
    return render(request, 'dashboard/factory_overview.html', context)

def factory(request):
    language_code = request.session['language_code']

    if request.method == "POST":
        language_en = request.POST.get('english', '')
        language_ms = request.POST.get('malay', '')
        if not language_en:
            language_code = language_ms
        else:
            language_code = language_en
    user_language = language_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    request.session['language_code'] = language_code

    now = datetime.datetime.now()

    factory_datas = Factory_Data.objects.filter(year=now.year).order_by('id')
    yields = Reports_Yield.objects.filter(report_id__year="2018")

    harvest_per_month = {}

    for single_yield in yields:
        if not single_yield.report_id.month_numeric in harvest_per_month:
            harvest_per_month[single_yield.report_id.month_numeric] = 0

        harvest_per_month[single_yield.report_id.month_numeric] += single_yield.harvested_amount_kg_banana

    graph_datas = {}

    for factory_data in factory_datas:
        graph_datas[factory_data.month] = factory_data.kgs_received

    graph_datas_converted = {}
    for i in range(1,13):

        if i in graph_datas:
            received = graph_datas[i]
        else:
            received = 0

        if i in harvest_per_month:
            kgs = harvest_per_month[i]
        else:
            kgs = 0

        graph_datas_converted[month_numbers_convert[i]] = {
            'received': received,
            'kgs': kgs
        }

    context = {
        'factory_datas': factory_datas,
        'graph_datas': graph_datas_converted
    }

    # Render the .html file
    return render(request, 'dashboard/factory.html', context)

def farmers(request):
    language_code = request.session['language_code']

    if request.method == "POST":
        language_en = request.POST.get('english', '')
        language_ms = request.POST.get('malay', '')
        if not language_en:
            language_code = language_ms
        else:
            language_code = language_en
    user_language = language_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    request.session['language_code'] = language_code

    farmers = Farm.objects.all()

    context = {
        'farmers': farmers
    }
    # Render the .html file
    return render(request, 'dashboard/farmers.html', context)

def harvests(request):
    language_code = request.session['language_code']

    if request.method == "POST":
        language_en = request.POST.get('english', '')
        language_ms = request.POST.get('malay', '')
        if not language_en:
            language_code = language_ms
        else:
            language_code = language_en
    user_language = language_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    request.session['language_code'] = language_code

    harvests = Reports_Yield.objects.select_related('report_id__farm__farmer').order_by('-report_id__year', '-report_id__month', '-id');

    harvest_per_month = {}

    for harvest in harvests:
        if not harvest.report_id.month in harvest_per_month:
            harvest_per_month[harvest.report_id.month] = {}
            harvest_per_month[harvest.report_id.month]['kgs'] = 0
            harvest_per_month[harvest.report_id.month]['number'] = 0

        harvest_per_month[harvest.report_id.month]['kgs'] = harvest_per_month[harvest.report_id.month]['kgs'] + harvest.harvested_amount_kg_banana
        harvest_per_month[harvest.report_id.month]['number'] = harvest_per_month[harvest.report_id.month]['number'] + harvest.harvested_amount_trees

    context = {
        'harvests': harvests,
        'harvest_per_month': harvest_per_month
    }

    # Render the .html file
    return render(request, 'dashboard/harvests.html', context)

def trees(request):
    language_code = request.session['language_code']

    if request.method == "POST":
        language_en = request.POST.get('english', '')
        language_ms = request.POST.get('malay', '')
        if not language_en:
            language_code = language_ms
        else:
            language_code = language_en
    user_language = language_code
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]

    request.session['language_code'] = language_code
    yields = Reports_Yield.objects.select_related('report_id__farm__farmer').order_by('-report_id__year', '-report_id__month', '-id'); #.filter(report_id__year="2018").

    planted_per_month = {}

    for row in yields:
        if not row.report_id.month in planted_per_month:
            planted_per_month[row.report_id.month] = 0

        planted_per_month[row.report_id.month] = planted_per_month[row.report_id.month] + row.planted_amount_trees


    context = {
        'rows': yields,
        'planted_per_month': planted_per_month
    }

    # Render the .html file
    return render(request, 'dashboard/trees.html', context)
