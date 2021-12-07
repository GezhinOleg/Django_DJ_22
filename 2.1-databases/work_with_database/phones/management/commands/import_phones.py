import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            model = Phone(
                name=phone.get('name'),
                price=float(phone.get('price')),
                image = phone.get('image'),
                release_date = phone.get('release_date'),
                lte_exists = phone.get('lte_exists'),
                slug = phone.get('name').lower()
            )
            model.save()
