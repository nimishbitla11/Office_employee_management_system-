from django.contrib import admin
from django.urls import path,include
from . views import *

urlpatterns = [
    path('index/',home),
    path('all_emp/',all_emp),
    path('add_emp/',add_emp),
    path('remove_emp/',remove_emp),
    path('remove_emp/<int:emp_id>',remove_emp),
    path('filter_emp/',filter_emp,name='filter_emp')

    
]
