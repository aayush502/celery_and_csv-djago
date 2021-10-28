from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import FileSerializer, CsvSerializer
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import *
from celery_show.tasks import *
import threading
from django.views.generic import View
import csv
import pdb



class FileView(APIView):
    def get(self, request):
        file = File.objects.all()
        serializer = FileSerializer(file, many=True)
        return Response(serializer.data)
    def post(self, request):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            try:
                thread = threading.Thread(target=file_serializer)
                thread.start()
                file_serializer.save()
                thread.join()
                # thread.join()
            except:
                print("File is not saved")
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CsvFile(APIView):
    def get(self, request):
        csv_file = Csv.objects.all()
        serializer = CsvSerializer(csv_file, many=True)
        return Response(serializer.data)
    def post(self, request):
        paramFile = request.FILES['file']
        decoded_file = paramFile.read().decode('utf-8').splitlines()
        # print(paramFile)
        from .tasks import parse_csv
        parse_csv.delay(decoded_file)


        return HttpResponse("file sent")

class index(View):
    def get(self, request):
        sleepy.delay(30)
        return HttpResponse("Hello World")
