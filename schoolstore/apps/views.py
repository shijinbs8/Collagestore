
from django.contrib import messages
from django.shortcuts import render

from .models import MyData

# Create your views here.


def index(request):
    return render(request,'home.html')
def home(request):
    return render(request,'index.html')
def forms(request):
    if request.method=='POST':
        Name=request.POST['name']
        last_Name=request.POST['lastname']
        DateOfBirth=request.POST['dob']
        Gender=request.POST['gender']
        Phone_number=request.POST['phonenumber']
        Email=request.POST['email']
        Department=request.POST['department']
        Courses=request.POST['courses']
        Purpose=request.POST['purpose']

        data = MyData(First_Name=Name,Last_Name=last_Name,DOB=DateOfBirth,Phone_Number=Phone_number,Email=Email,Gender=Gender
                      ,Department=Department,Course=Courses,Purpose=Purpose)
        messages.success(request, "Order Confirmed")
        data.save()
    return render(request,'forms.html')

