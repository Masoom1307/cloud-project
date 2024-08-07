from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): 

    return render(request, 'lmsreporting/home.html')

def about(request): 

    return render(request, 'lmsreporting/about.html')


def contact(request): 

    return render(request, 'lmsreporting/contact.html')


def modules(request): 

    return render(request, 'lmsreporting/modules.html')
