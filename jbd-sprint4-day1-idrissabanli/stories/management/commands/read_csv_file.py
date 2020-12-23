import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from stories.models import Category



class Command(BaseCommand):
    help = 'Displays command working or not'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, help='Read line count')
        parser.add_argument('--filename', type=str, help='get file name form user')

    def handle(self, *args, **kwargs):
        # print(kwargs['count'])
        filename = kwargs['filename']
        filename = os.path.join(settings.BASE_DIR, filename)
        self.stdout.write("Command Working")
        with open(filename, 'r') as f:
            fieldnames = ['title', 'image']
            csv_reader = csv.DictReader(f, fieldnames=fieldnames)
            for row in csv_reader:
                Category.objects.create(title=row['title'], image=row['image'])



