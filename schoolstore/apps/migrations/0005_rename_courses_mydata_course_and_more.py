# Generated by Django 4.1.7 on 2023-02-20 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0004_mydata_courses_mydata_dateofbirth_mydata_department_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="mydata",
            old_name="Courses",
            new_name="Course",
        ),
        migrations.RenameField(
            model_name="mydata",
            old_name="Phone_number",
            new_name="Phone_Number",
        ),
        migrations.RemoveField(
            model_name="mydata",
            name="DateOfBirth",
        ),
        migrations.RemoveField(
            model_name="mydata",
            name="Gender",
        ),
        migrations.AddField(
            model_name="mydata",
            name="DOB",
            field=models.CharField(default=12.2, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="mydata",
            name="Email",
            field=models.CharField(max_length=100),
        ),
    ]
