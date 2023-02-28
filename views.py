from genericpath import exists
from unicodedata import name
from django.shortcuts import render
from.models import phonebook

# Create your views here.
def phn(request):
    return render(request,'home.html')

def addnumber(request): 
    phndic={}
    try:
            name=request.POST['name']
            phnnumber=int(request.POST['number'])
            list1=phonebook.objects.filter(Name=name)
            if list1.exists():
                phndic['msg']='already exists'
                return render(request,'home.html',phndic)
            else:
                emplist=phonebook(Name=name,Number=phnnumber)
                emplist.save()
                phndic['msg']='name and phone number added'
                return render(request,'home.html',phndic)
    except Exception as b:
            print(b)
            phndic['msg']='name is not addaed'        
            return render(request,'home.html',phndic)
            # if name in phndic:
            #     return render(request,'index.html',{'ex':'already undu'})
            # else:





def display(request):
    empdtls=phonebook.objects.all()
    return render(request,'home.html',{'emp':empdtls})

def update(request):
    try:
        oldname=request.POST['oldname']
        newname=request.POST['newname']
        if oldname==newname:
            return render(request,'index.html',{'key':'already exist'})
        phonebook.objects.filter(Name=oldname).update(Name=newname)
        return render(request,'home.html',{'UPDATE':'Updated'})
    except Exception as b:
        print(b)
        return render(request,'home.html',{'UPDATE':'Not Updated'})

def delete(request):
    
    try:
        dlt=request.POST['dlt']
        phonebook.objects.filter(Name=dlt).delete()
        return render (request,'home.html',{'del':'deleted'})
    except Exception as b:
        print(b)
        return render (request,'home.html',{'del':' Not Done'})

def updatenumber(request):
    return render(request,'index.html',{'update number':''})






