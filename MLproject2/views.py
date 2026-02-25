from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
# FILE UPLOAD AND VIEW
from  django.core.files.storage import FileSystemStorage
# SESSION
from django.conf import settings
from .models import *
from django.db.models import F
from ML import test
from tensorflow.keras import backend as K
import os
def home(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')
def register(request):
    return render(request,'register.html')
def feedback(request):
    return render(request,'feedback.html')

def addregister(request):
    if request.method=="POST":
        a=request.POST.get('Name') 
        b=request.POST.get('Email')
        c=request.POST.get('Password')
        d=request.POST.get('Phone')   
        ins=regtable(name=a,email=b,password=c,phone=d)
        ins.save()
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def addlogin(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    if email=='admin@gmail.com'and password=='admin':
       request.session['admin@gmail.com']='admin@gmail.com'
       request.session['admin']='admin'
       ins=regtable.objects.all()
       return render(request,'index.html')

    if regtable.objects.filter(email=email,password=password).exists():
        userdetails=regtable.objects.get(email=email,password=password)
        if userdetails.email==request.POST['email']:
            request.session['userid']=userdetails.id
            request.session['username']=userdetails.name 
            return render(request,'index.html')  
    else:
         return render(request,'login.html')

def logout(request):
    session_keys=list(request.session.keys())   
    for key in session_keys:
            del request.session[key] 
    return redirect(index) 

def upload(request):
    return render(request,'upload.html')
    
def addupload(request):
    if request.method == "POST":
        file=request.FILES['file'] 
        fs=FileSystemStorage()
        filename=fs.save(file.name,file)
        try:
            os.remove(os.path.join(settings.MEDIA_ROOT, 'input/test/test.csv'))
        except:
            pass

        fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'input/test'))
        fs.save("test.csv", file)
        fs = FileSystemStorage()
        fs.save(file.name, file)
        K.clear_session()

        result = test.predict()
        ins=uploadtable(images=filename,user_id=request.session['userid'],result=result)
        ins.save()
    return render(request,'upload.html',{'result':result})

def viewuser(request):
    user=regtable.objects.all()
    return render(request,'viewuser.html',{'result':user})   

def viewupload(request):
    user=uploadtable.objects.filter(user_id=request.session['userid'])
    return render(request,'viewupload.html',{'result':user})    

def viewuploads(request):
    user=uploadtable.objects.all()
    return render(request,'viewuploads.html',{'result':user}) 
def addfeedback(request):
    if request.method=="POST":
        a=request.POST.get('message') 
       
        ins=feedtable(message=a)
        ins.save()
    return render(request,'feedback.html')

def viewfeedback(request):
    user=feedtable.objects.all()
    return render(request,'viewfeedback.html',{'result':user}) 