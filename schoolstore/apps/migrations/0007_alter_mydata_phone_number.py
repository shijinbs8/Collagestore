# Generated by Django 4.1.7 on 2023-02-20 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0006_mydata_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mydata",
            name="Phone_Number",
            field=models.CharField(max_length=100),
        ),
    ]
