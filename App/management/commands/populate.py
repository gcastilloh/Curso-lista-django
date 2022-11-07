from django.core.management import BaseCommand
from faker import Faker

from App.models import Employee
from random import randrange


class Command(BaseCommand):
    def handle(self, *args, **options):
        occupattion_list = [
            'actress', 'actor', 'architect', 'singer', 'dentist',
            'detective', 'writer', 'farmer', 'nurse', 'pilot',
            'engineer', 'accountant', 'butcher', 'cashier','barber',
            'carpenter', 'lifeguard', 'baker', 'electrician','flight attendant',
            'plumber', 'receptionist', 'researcher', 'scientist',
            'lawyer', 'bus driver', 'designer',
        ]
        gender_list = ['M','F']

        faker = Faker()
        print('Adding 500 records to Products model')
        print(f'Before we have: {Employee.objects.all().count()} employees')
        for _ in range(500):
            Employee.objects.create(
                name = faker.name(),
                occupation = occupattion_list[randrange(0,len(occupattion_list))],
                salary = randrange(1000,5000),
                gender = gender_list[randrange(0,2)],
                email = faker.email(),
            )
        print(f'Now we have: {Employee.objects.all().count()} employees')

