from os import name
from django.urls import path
from .views import CsvFile, FileView

urlpatterns = [
    path('upload/', FileView.as_view(), name="upload"),
    path('csv/', CsvFile.as_view(), name="csv"),
]