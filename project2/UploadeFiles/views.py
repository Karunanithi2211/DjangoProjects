import os
from django.shortcuts import render, redirect
from .forms import MyFileForm
from .models import MyFileUpload
from django.contrib import messages

# Create your views here.
def home(req):
    mydata=MyFileUpload.objects.all()
    myform=MyFileForm()
    if mydata!='':
        context={'form':myform,'mydata':mydata}
        return render(req,'index.html',context)
    else:
        context = {'form':myform}
        return render(req,'index.html',context)

def uploadfile(req):
    if req.method=="POST":
        myform=MyFileForm(req.POST,req.FILES)
        if myform.is_valid():
            MyFileName=req.POST.get('file_name')
            MyFile = req.FILES.get('file')
            exists=MyFileUpload.objects.filter(my_file=MyFile).exists()
            if exists:
                messages.error(req,'The file %s is already exists...!!!' %MyFile)
            else:
                MyFileUpload.objects.create(file_name=MyFileName,my_file=MyFile).save()
                messages.success(req,'File uploaded successfully')
        return redirect('home')
    
def deletefile(req,id):
    mydata=MyFileUpload.objects.get(id=id)
    mydata.delete()
    os.remove(mydata.my_file.path)
    messages.success(req,"File deleted successfully")
    return redirect('home')