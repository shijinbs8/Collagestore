# Generated by Django 4.1.7 on 2023-02-19 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0002_mydata"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="mydata",
            name="Courses",
        ),
        migrations.RemoveField(
            model_name="mydata",
            name="DateOfBirth",
        ),
        migrations.RemoveField(
            model_name="mydata",
            name="Department",
        ),
        migrations.RemoveField(
            model_name="mydata",
            name="Email",
        ),
        migrations.RemoveField(
            model_name="mydata",
            name="Gender",
        ),
        migrations.RemoveField(
            model_name="mydata",
            name="Last_Name",
        ),
        migrations.RemoveField(
            model_name="mydata",
            name="Phone_number",
        ),
        migrations.RemoveField(
            model_name="mydata",
            name="Purpose",
        ),
    ]