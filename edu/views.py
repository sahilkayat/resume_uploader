from django.shortcuts import render

# Create your views here.
def skill(requests):
    context = {'skill': 'active'}
    return render(requests,'edu/skill.html',context)