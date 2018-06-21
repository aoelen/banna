from django.shortcuts import get_object_or_404, render, redirect

from farmer.models import YieldForm
from farmer.models import Yield

#SHOW OVERVIEW YIELD
def overview_yield(request, id=id):
    latest_yield_list = Yield.objects.all()
    context = {'latest_yield_list': latest_yield_list}
    return render(request, './overview/yield.html', context)


#ADD YIELD
def add_yield(request):
    print("hallo world")
    if request.method == "POST":
        print("post method started")
        form = YieldForm(request.POST)
        if form.is_valid():
            print("form is valid")
            yield_item = form.save(commit=False)
            yield_item.save()
            return redirect('/farmer/yield')
    else:
        form = YieldForm()
    return render(request, './add/yield.html', {'yield':form})

#EDIT YIELD
def edit_yield(request, id=None):
    item = get_object_or_404(Yield, id=id)
    form = YieldForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/yield/')
    return render(request, './edit/yield.html', {'yield':form})


#DELETE YIELD
def delete_yield(request, id=id):
    yield_id = Yield.objects.get(pk=id) #get yield which needed be deleted
    yield_id.delete()
    return redirect('/farmer/yield/')