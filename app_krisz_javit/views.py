from django.shortcuts import render

# Create your views here.


def app_krisz_javit(request):
    context= {}
    return render(request, 'app_krisz_javit/index.html',context)
