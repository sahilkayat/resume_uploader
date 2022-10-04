from django.shortcuts import render

# Create your views here.
def home(requests):
    
    return render(requests,'core/home.html',{'home': 'active'})

def contact(requests):
    
    return render(requests,'core/contact.html',{'contact': 'active'})
