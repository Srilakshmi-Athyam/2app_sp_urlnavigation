from django.urls import path
from app2.views import *
app_name='grape'
urlpatterns=[
    path('grape/',grape,name='grape')
]