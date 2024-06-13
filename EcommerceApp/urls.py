from django.urls import path
#now import the views.py file into this code
from .migrations import views
from . import views
urlpatterns=[
path('home/',views.index,name='home')
]
