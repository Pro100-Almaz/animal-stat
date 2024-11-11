from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *

def welcome(request):
    return render(request, 'welcome.html')

def index(request):
    return render(request, 'index.html')

def define_percent(val1, val2):
    if val2 == 0:
        return 0
    return round(100 * (val1 - val2) / val2, 3)

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
                difference_in_total -= record.total
                first_year_total = record.total
                break

        for record in records:
            if record.year == int(second_val):
                difference_in_total += record.total
                percentage = {}
                percentage['number'] = round(difference_in_total / first_year_total * 100, 3)
                percentage['first_val'] = first_val
                percentage['second_val'] = second_val

                return render(request, 'crime.html', {'percentage': percentage, 'records' : records, 'saiga_total': saiga_total, 'red_book_total': red_book_total, 'other_total': other_total, 'total_total': total_total})


    return render(request, 'crime.html', {'percentage': False, 'records' : records, 'saiga_total': saiga_total, 'red_book_total': red_book_total, 'other_total': other_total, 'total_total': total_total})


def add_crime(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        saiga = request.POST.get("saiga")
        red_book = request.POST.get("red_book")
        others = request.POST.get("others")
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

    percentage = {}

    if request.method == 'POST':
        data = request.POST.getlist('data')

        first_val = TakenItems.objects.get(id = data[-2])
        second_val = TakenItems.objects.get(id = data[-1])

        percentage['first_val'] = first_val.year
        percentage['second_val'] = second_val.year

        percentage['saiga_without_horns'] = define_percent(second_val.saiga_without_horns, first_val.saiga_without_horns) 
        percentage['saiga_with_horns'] = define_percent(second_val.saiga_with_horns, first_val.saiga_with_horns) 
        percentage['saiga_female'] = define_percent(second_val.saiga_female, first_val.saiga_female) 
        percentage['horns'] = define_percent(second_val.horns, first_val.horns) 
        percentage['segoltok'] = define_percent(second_val.segoltok, first_val.segoltok) 
        percentage['arhar'] = define_percent(second_val.arhar, first_val.arhar) 
        percentage['jeiran'] = define_percent(second_val.jeiran, first_val.jeiran) 
        percentage['drofa'] = define_percent(second_val.drofa, first_val.drofa) 
        percentage['qulan'] = define_percent(second_val.qulan, first_val.qulan) 
        percentage['sadja'] = define_percent(second_val.sadja, first_val.sadja) 
        percentage['falcon'] = define_percent(second_val.falcon, first_val.falcon) 
        percentage['podorlik'] = define_percent(second_val.podorlik, first_val.podorlik) 
        percentage['falcon_baloban'] = define_percent(second_val.falcon_baloban, first_val.falcon_baloban) 
        percentage['sturgeon'] = define_percent(second_val.sturgeon, first_val.sturgeon) 
        percentage['badger'] = define_percent(second_val.badger, first_val.badger) 


    return render(request, 'crime_item.html', {'records': records, 'percentage': percentage})


def add_crime_item(request):
    if request.method == 'POST':
        year = request.POST.get('year')
        saiga_without_horns = request.POST.get("saiga_without_horns")
        saiga_with_horns = request.POST.get("saiga_with_horns")
        saiga_female = request.POST.get("saiga_female")
        horns = request.POST.get("horns")
        segoltok = request.POST.get("segoltok")
        arhar = request.POST.get("arhar")
        jeiran = request.POST.get("jeiran")
        drofa = request.POST.get("drofa")
        qulan = request.POST.get("qulan")
        sadja = request.POST.get("sadja")
        falcon = request.POST.get("falcon")
        podorlik = request.POST.get("podorlik")
        falcon_baloban = request.POST.get("falcon_baloban")
        sturgeon = request.POST.get("sturgeon")
        badger = request.POST.get("badger")

        try:
            record = TakenItems.objects.get(year=year)
            record.saiga_without_horns = saiga_without_horns
            record.saiga_with_horns = saiga_with_horns
            record.saiga_female = saiga_female
            record.horns = horns
            record.segoltok = segoltok
            record.arhar = arhar
            record.jeiran = jeiran
            record.drofa = drofa
            record.qulan = qulan
            record.sadja = sadja
            record.falcon = falcon
            record.podorlik = podorlik
            record.falcon_baloban = falcon_baloban
            record.sturgeon = sturgeon
            record.badger = badger
            
        except TakenItems.DoesNotExist:
            new_data = TakenItems.objects.create(year=year, 
                                                saiga_without_horns=saiga_without_horns, 
                                                saiga_with_horns = saiga_with_horns,
                                                saiga_female = saiga_female,
                                                horns = horns,
                                                segoltok = segoltok,
                                                arhar = arhar,
                                                jeiran = jeiran,
                                                drofa = drofa,
                                                qulan = qulan,
                                                sadja = sadja,
                                                falcon = falcon,
                                                podorlik = podorlik,
                                                falcon_baloban = falcon_baloban,
                                                sturgeon = sturgeon,
                                                badger = badger)
            new_data.save()


        return HttpResponseRedirect('/crime_item/')
    else:
        return render(request, 'add_crime_item.html')

def animal_list(request):
    animal_list = AnimalName.objects.all()

    return render(request, 'animals.html', {'animal_list': animal_list})

def animal_view(request, name):
    animal_name = AnimalName.objects.get(name = name)
    location_of_animal = Location.objects.filter(name__name=animal_name)
    records = AnimalData.objects.filter(animal__in=location_of_animal).order_by('year')

    years = []

    for record in records:
        if record.year not in years:
            years.append(record.year)

    data_by_year = {year: [] for year in years}

    for record in records:
        data_by_year[record.year].append(record.number)

    if request.method == 'POST':
        data = request.POST.getlist('data')

        first_val = AnimalData.objects.get(id = data[-2])
        second_val = AnimalData.objects.get(id = data[-1])

        first_year_total = 0
        difference_in_total = 0

        percentage = {}
        percentage['first_val'] = first_val.year
        percentage['second_val'] = second_val.year
        percentage['region1'] = first_val.animal.region
        percentage['region2'] = second_val.animal.region

        for record in records:
            if record.year == int(first_val.year):
                if record.number:
                    difference_in_total -= record.number
                    first_year_total = record.number
                else:
                    percentage['number'] = 0
                    return render(request, 'animal.html', {'locations': location_of_animal, 'percentage': percentage, 'records': records, 'name': name, 'data_by_year': data_by_year})
                  
                break

        for record in records:
            if record.year == int(second_val.year):
                if record.number:
                    difference_in_total += record.number
                else :
                    difference_in_total = 0

                percentage['number'] = round(difference_in_total / first_year_total * 100, 3)

                return render(request, 'animal.html', {'locations': location_of_animal, 'percentage': percentage, 'records': records, 'name': name, 'data_by_year': data_by_year})

    return render(request, 'animal.html', {'locations': location_of_animal, 'records': records, 'name': name, 'data_by_year': data_by_year})

def add_animal(request, name):
    animal_name = AnimalName.objects.get(name = name)
    location_of_animal = Location.objects.filter(name__name=animal_name)
    records = AnimalData.objects.filter(animal__in=location_of_animal)

    if request.method == 'POST':
        year = request.POST.get('year')
        region = request.POST.get("region")
        number = request.POST.get("number")

        try:
            location_of_animal = Location.objects.get(name__name=animal_name, region = region)
        except Location.DoesNotExist:
            location_of_animal = Location.objects.create(name__name=animal_name, region = region)

        try:
            record = AnimalData.objects.get(animal=location_of_animal, year = year)
            record.number = number
        except AnimalData.DoesNotExist:
            AnimalData.objects.create(year=year, animal=location_of_animal, number = number)

        location_of_animal = Location.objects.filter(name__name=animal_name)
        records = AnimalData.objects.filter(animal__in=location_of_animal)
        return render(request, 'animal.html', {'records': records, 'name': name})
    
    return render(request, 'add_animal.html')
