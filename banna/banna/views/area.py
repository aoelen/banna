from django.shortcuts import get_object_or_404, render, redirect

from ..models.modalforms import AreaForm
from ..models.models import Area

#SHOW OVERVIEW CATEGORIES
def overview_areas(request, id=id):
    latest_area_list = Area.objects.all()
    context = {'latest_area_list': latest_area_list}
    return render(request, '/overview/areas.html', context)


#ADD CATEGORY
def add_area(request):
    if request.method == "POST":
        form = AreaForm(request.POST)
        if form.is_valid():
            area_item = form.save(commit=False)
            area_item.save()
            return redirect('overview/areas')
    else:
        form = AreaForm()
    return render(request, '/add/area.html', {'area':form})

#EDIT CATEGORY
def edit_area(request, id=None):
    item = get_object_or_404(Area, id=id)
    form = AreaForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/area/')
    return render(request, '/edit/area.html', {'area':form})


#DELETE CATEGORY
def delete_area(request, id=id):
    area = Area.objects.get(pk=id) #get area which needed be deleted
    area.delete()
    return redirect('overview/areas')