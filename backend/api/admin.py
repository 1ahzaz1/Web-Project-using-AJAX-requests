from django.contrib import admin
from .models import Person, Motorbike, Ride

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth')
    search_fields = ('name',)

@admin.register(Motorbike)
class MotorbikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'engine_capacity', 'is_automatic')
    search_fields = ('name',)

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('person', 'motorbike', 'is_favourite')
    search_fields = ('person__name', 'motorbike__name')
