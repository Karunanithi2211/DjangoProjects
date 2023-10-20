from django.shortcuts import render,redirect
from .models import Datas
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, "Home.html", {"Name":"Kavin"})
#     msg = "<h1>Welcome to Django Frameworks bro!</h1>"
#     return HttpResponse(msg)
# def Home1(request):
#     msg = "<h1>Welcome to the next page bro!</h1>"
#     return HttpResponse(msg)
def Home1(req):
    return render(req,"Home1.html",{'Name':'KAVIN2211'})

def Form(requests):
    return render(requests, "form.html")

def product(val):
    mobile=int(val.GET['Mobile'])
    keyboard=int(val.GET['Keyboard'])
    monitor=int(val.GET['Monitor'])
    price = mobile + keyboard + monitor
    return render(val, "result.html", {"price":price})

def Form1(req):
    return render(req, "Form1.html")

def OutputF1(val):
    name = val.POST['name']
    password = val.POST['password']
    email = val.POST['email']
    number = val.POST['number']
    return render(val, 'OutputF1.html', {'Name':name, 'Password':password, 'Email':email, 'Number':number})

def static(req):
    return render(req,'static.html')

def bootstrap(req):
    return render(req, "Bootstrap.html")

def mvt(re):
    mydatas=Datas.objects.all()
    if (mydatas == ''):
        return render(re,'mvt.html')
    else:
        return render(re,'mvt.html', {'data':mydatas})
    
def dataadd(req):
    if req.method=='POST':
        name=req.POST['name']
        age=req.POST['age']
        address=req.POST['address']
        contact=req.POST['contact']
        mail=req.POST['mail']
        
        obj = Datas()
        obj.Name=name
        obj.Age=age
        obj.Address=address
        obj.Contact=contact
        obj.Mail=mail
        obj.save()
        
        mydatas=Datas.objects.all()
        return redirect('mvt')
    return render(req,'mvt.html',{'data':mydatas})

def update(r,id):
    iddatas = Datas.objects.get(id=id)
    if r.method == 'POST':
        name=r.POST['name']
        age=r.POST['age']
        address=r.POST['address']
        contact=r.POST['contact']
        mail=r.POST['mail']
        
        iddatas.Name=name
        iddatas.Age=age
        iddatas.Address=address
        iddatas.Contact=contact
        iddatas.Mail=mail
        iddatas.save()
        return redirect('mvt')
         
    return render(r,'mvt_update.html',{'data':iddatas})

def delete(r,id):
    deledata = Datas.objects.get(id=id)
    deledata.delete()
    return redirect('mvt')