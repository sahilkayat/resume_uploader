from django.shortcuts import render

# Create your views here.
def services(requests):
    context = {'services': 'active'}
    return render(requests,'serv/services.html',context)
