from django.urls import path
from app1.views import *
app_name='mango'
urlpatterns=[
    path('mango/',mango,name='mango')
]