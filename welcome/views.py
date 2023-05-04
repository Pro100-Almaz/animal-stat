from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
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
    ind = 0

    for record in records:
        if ind > 0 :
            record.percentage = round((records[ind].total - records[ind-1].total) / records[ind-1].total * 100, 3)

        saiga_total += record.saiga
        red_book_total += record.red_book
        other_total += record.others
        total_total += record.total
        ind += 1

    
    if request.method == 'POST':
        data = request.POST.getlist('data')

        first_val = data[-2]
        second_val = data[-1]

        first_year_total = 0
        difference_in_total = 0

        for record in records:
            if record.year == int(first_val):
                difference_in_total = record.total
                first_year_total = record.total
                break

        for record in records:
            if record.year == int(second_val):
                difference_in_total -= record.total
                percentage = {}
                percentage['number'] = round(difference_in_total / first_year_total * 100, 3)
                percentage['first_val'] = first_val
                percentage['second_val'] = second_val

                return render(request, 'crime.html', {'percentage': percentage, 'records' : records, 'saiga_total': saiga_total, 'red_book_total': red_book_total, 'other_total': other_total, 'total_total': total_total})


    return render(request, 'crime.html', {'percentage': False, 'records' : records, 'saiga_total': saiga_total, 'red_book_total': red_book_total, 'other_total': other_total, 'total_total': total_total})


def add_crime(request):
    print("AINASDAS")
    if request.method == 'POST':
        year = request.POST.get('year')
        saiga = request.POST.get("saiga")
        red_book = request.POST.get("red_book")
        others = request.POST.get("others")
        print("In post fcuntoien")
        try:
            record = CrimeNumber.objects.get(year=year)
            record.saiga = saiga
            record.red_book = red_book
            record.others = others
            record.calculate_total()
            record.save()
        except CrimeNumber.DoesNotExist:
            new_data = CrimeNumber.objects.create(year=year, saiga=saiga, red_book=red_book, others=others, total = 0)
            new_data.calculate_total()
            new_data.save()


        return HttpResponseRedirect('/crime/')
    else:
        return render(request, 'add_crime.html')

def crime_item_number(request):
    records = TakenItems.objects.all().order_by('year')

    return render(request, 'crime_item.html', {'records': records})
