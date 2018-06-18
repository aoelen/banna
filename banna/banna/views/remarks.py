from django.shortcuts import get_object_or_404, render, redirect

from ..models.modalforms import RemarkForm
from ..models.models import Remark

#SHOW OVERVIEW REMARKS
def overview_remarks(request, id=id):
    latest_remarks_list = Remark.objects.all()
    context = {'latest_remarks_list': latest_remarks_list}
    return render(request, '/overview/remarks.html', context)

#ADD REMARK
def add_remark(request):
    if request.method == "POST":
        form = Remark(request.POST)
        if form.is_valid():
            remark_item = form.save(commit=False)
            remark_item.save()
            return redirect('overview/remark')
    else:
        form = RemarkForm()
    return render(request, '/add/remark.html', {'remark':form})

#EDIT REMARK
def edit_remark(request, id=None):
    item = get_object_or_404(Remark, id=id)
    form = RemarkForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/remark/')
    return render(request, '/edit/remark.html', {'remark':form})


#DELETE REMARK
def delete_remark(request, id=id):
    remark = Remark.objects.get(pk=id) #get remark which needed be deleted
    remark.delete()
    return redirect('overview/remark')