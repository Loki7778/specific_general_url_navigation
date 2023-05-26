from django.shortcuts import render

# Create your views here.
def bank(request):
    d={'age':23}
    return render(request,'bank.html',context=d)