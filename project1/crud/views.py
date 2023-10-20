from django.shortcuts import render,redirect
from .forms import Myformcrud
from django.contrib import messages
from .models import Registerform
# Create your views here.


def homecrud(r):
    datas = Registerform.objects.all()
    if (datas != ''):
        return render (r,'homecrud.html', {'datas':datas})
    else:
        return render(r,"homecrud.html") 

def insertcrud(r):
    if r.method=='POST':
        formcrud = Myformcrud(r.POST)
        if formcrud.is_valid:
            try:
                formcrud.save()
                messages.success(r,"Registered Successfully")
                return redirect('home')
            except:
                pass
    else:
        formcrud = Myformcrud()
    return render(r,'registercrud.html',{'formcruds': formcrud})

def updatecrud(r,id):
    data = Registerform.objects.get(id=id) 
    if r.method == 'POST':
        name = r.POST['name']
        age = r.POST ['age']
        address = r.POST['address']
        contact = r.POST['contact']
        email = r.POST['email']
        
        data.name=name
        data.age=age
        data.address=address
        data.contact=contact
        data.email=email
        
        data.save()
        
        messages.success(r,'Updated Successfully')
        return redirect('home')

    return render(r,'updatecrud.html', {'data':data})

def deletecrud(r,id):
    data=Registerform.objects.get(id=id)
    data.delete()
    messages.error(r,'Deleted Successfully')
    return redirect('home')
      
    