from django.shortcuts import render,redirect
from .forms import DateForm
def home_page(request):
    return render(request, 'meet/home.html')
def pick_a_date(request):
    form=DateForm()
    if request.method=='POST':
        form=DateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    context={'form':form}
    return render(request, 'meet/pick_a_date.html',context)
def success(request):
    return render(request, 'meet/success.html')