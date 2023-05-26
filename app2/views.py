from django.shortcuts import render

# Create your views here.
def bank2(request):
    d={'name':'sai'}
    return render(request ,'bank2.html',context=d)