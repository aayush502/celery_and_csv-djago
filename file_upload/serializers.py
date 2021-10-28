from django.db.models import fields
from rest_framework import serializers
from .models import Csv, File

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = File
    fields = ('file', 'remark', 'timestamp')

class CsvSerializer(serializers.ModelSerializer):
  class Meta():
    model = Csv
    fields = "__all__"