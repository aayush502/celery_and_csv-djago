# Generated by Django 3.2.8 on 2021-10-20 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='remark',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
