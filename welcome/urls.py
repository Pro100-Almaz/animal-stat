from welcome.views import welcome, index, crime_number, add_crime, crime_item_number
from django.urls import path

urlpatterns = [
    path("", welcome, name='welcome'),
    path("index/", index, name="index"),
    path("crime/", crime_number, name="crime_number"),
    path("add_crime/", add_crime, name="add_crime"),
    path("crime_item/", crime_item_number, name="crime_item_number"),
    
]