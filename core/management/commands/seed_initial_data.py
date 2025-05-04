from django.core.management.base import BaseCommand
from apps.advertisements.models import (
    CategoryModel,
    TransmissionModel,
    FuelTypeModel,
    StatusModel,
)


class Command(BaseCommand):
    help = 'Seeds the database with initial categories, transmissions and fuel types'

    def handle(self, *args, **kwargs):
        category_names = ["Sedan", "Station Wagon", "Hatchback", "SUV", "Coupe", "Convertible"]
        transmission_names = ["Manual", "Automatic", "Robot", "CVT"]
        fuel_type_names = ["Petrol", "Diesel", "Gas", "Electric", "Hybrid"]
        status_names = ["Available", "In Service", "Idle", "Broken", "Booked"]

        existing_categories = set(CategoryModel.objects.values_list('name', flat=True))
        existing_transmissions = set(TransmissionModel.objects.values_list('name', flat=True))
        existing_fuel_types = set(FuelTypeModel.objects.values_list('name', flat=True))
        existing_statuses = set(StatusModel.objects.values_list('name', flat=True))

        new_categories = [
            CategoryModel(name=name) for name in category_names if name not in existing_categories
        ]
        new_transmissions = [
            TransmissionModel(name=name) for name in transmission_names if name not in existing_transmissions
        ]
        new_fuel_types = [
            FuelTypeModel(name=name) for name in fuel_type_names if name not in existing_fuel_types
        ]
        new_statuses = [
            StatusModel(name=name) for name in status_names if name not in existing_statuses
        ]

        CategoryModel.objects.bulk_create(new_categories)
        TransmissionModel.objects.bulk_create(new_transmissions)
        FuelTypeModel.objects.bulk_create(new_fuel_types)
        StatusModel.objects.bulk_create(new_statuses)

        self.stdout.write(self.style.SUCCESS('Initial data seeded successfully with bulk_create.'))
