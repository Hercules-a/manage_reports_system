from django.contrib import admin
from .models import Problem, Order, Part, Car, PartStage


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('number', 'description')


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')


@admin.register(PartStage)
class PartStageAdmin(admin.ModelAdmin):
    list_display = ('part', 'stage')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('number', 'parts', 'measuring_specification')
