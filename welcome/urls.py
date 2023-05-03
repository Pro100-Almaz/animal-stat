from welcome.views import welcome, index
from django.urls import path

urlpatterns = [
    path("", welcome, name='welcome'),
    path("index/", index, name="index")
]