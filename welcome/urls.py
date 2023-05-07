from welcome.views import *
from django.urls import path

urlpatterns = [
    path("", welcome, name='welcome'),
    path("index/", index, name="index"),
    path("crime/", crime_number, name="crime_number"),
    path("add_crime/", add_crime, name="add_crime"),
    path("crime_item/", crime_item_number, name="crime_item_number"),
    path("add_crime_item/", add_crime_item, name="add_crime_item"),
    path("animals/", animal_list, name="animal_list"),
    path("animal/<str:name>/", animal_view, name="animal_view"),    
    path("add_animal/<str:name>/", add_animal, name="add_animal"),    
]