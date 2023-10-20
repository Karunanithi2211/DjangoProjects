from django.shortcuts import render,redirect
from .forms import createuserform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(r):
    return render(r,'home.html')

def login(r):
    return render(r,'login.html')

def register(r):
    if r.method == 'POST':
        username = r.POST['username']
        email = r.POST['email']
        password1 = r.POST['password1']
        password2 = r.POST['password2']
        
        if password1==password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            messages.success(r,'You have registered successfull, You can login')
            return redirect('lo')
        else:
            messages.warning(r,'Password Missmatching.....!!!')
            return redirect('re')
    else:
        form1 = createuserform()
        return render(r,'register.html', {'form':form1})
 
@login_required   
def profile(r):
    return render(r,'profile.html')
    
# def logout(r):
#     return render(r,'logout.html')