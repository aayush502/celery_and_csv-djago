import csv
from .models import Csv
from celery import shared_task
from storage_file.celery import app
import pdb

@shared_task
def parse_csv(decoded_file):
    data = csv.DictReader(decoded_file)
    list1 = []
    for row in data:
        final = dict(row)
        list1.append(final)
    Csv.create_data(list1)
    return list1