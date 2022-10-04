from django.shortcuts import render

# Create your views here.
def home(requests):
    context = {'home': 'active'}
    return render(requests,'core/home.html',context)

def contact(requests):
    context = {'contact': 'active'}
    return render(requests,'core/contact.html',context)