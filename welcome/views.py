from django.shortcuts import render
from .models import *

def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    return render(request, 'index.html')

def crime_number(request):
    records = CrimeNumber.objects.all().order_by('year')

    saiga_total = 0
    red_book_total = 0
    other_total = 0
    total_total = 0

    for record in records:
        saiga_total += record.saiga
        red_book_total += record.red_book
        other_total += record.others
        total_total += record.total
        
    return render(request, 'crime.html', {'records' : records, 'saiga_total': saiga_total, 'red_book_total': red_book_total, 'other_total': other_total, 'total_total': total_total})

def add_crime(request):
    if request.POST:
        year = request.POST["year"]
        saiga = request.POST["saiga"]
        red_book = request.POST["red_book"]

    return render(request, 'add_crime.html')
