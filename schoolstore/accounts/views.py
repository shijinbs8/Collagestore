
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,HttpResponse




def login(request):
    if request.method == 'POST':
        username = request.POST["name"]
        password2 = request.POST["password"]
        user = auth.authenticate(username=username, password=password2)
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html')
        else:
            messages.info(request,"Invalid Login")
            return redirect('/accounts/login/')
    return render(request,'login.html')


def register(request):
    if request.method == 'POST':
        username1 = request.POST["name"]
        password1 = request.POST['password']
        cpassword = request.POST['cpassword']
        if password1 == cpassword:
            if User.objects.filter(username=username1).exists():
                messages.info(request,'Username Taken')
                return redirect('/accounts/register/')

            else:
                user = User.objects.create_user(username=username1,password=password1)
                user.save();
                print("user created")
                return redirect('/accounts/login/')
        else:
            messages.info(request,"Password not matching")
            print('passwordnotmatching')
            return redirect('/accounts/register/')

        return redirect('login')
    return render(request,'Register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.
