from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from myapp.form import EmpForm

import pymongo
import datetime


cli=pymongo.MongoClient('mongodb://localhost:27017')
mydta=cli['django']
mytba=mydta['app']
mytba.find()
'''
def index(request):
    name=mytba.find({})
    print(name)
    templtae=loader.get_template('index.html')
    data={'data':name}
    return render(request,"index.html",data)
'''        
    
    

def home(request):
    html="<html><body><h3>Now time is %s.</h3></body></html>" % datetime.datetime.now()
    return HttpResponse(html)
def mongo(request):
    data={
        "name":"pandu"
    }
    mytba.insert_one(data)
    print("1 row added")
    return HttpResponse("data added ")
def data(request):
    data=mytba.find({})
    
    
    gog={'name':data}
    
    return render(request,"index.html",gog)

def delete(request,name):
    myqu={
        "name":name
    }
    mytba.delete_one(myqu)
    print("deleted sucessfully")
    return redirect('/')


def edit(request,name):
   
    
    gog={
        "name":name
    }
   
    return render(request,"update.html",gog)
def update(request,name):
    olddata={
        "name":name
    }
    newdata=request.POST.get('name')
    newque={
        "$set":{
            "name":newdata
        }
    }
    mytba.update_one(olddata,newque)
    return redirect('/',olddata)



  
    
    
def formss(request):
  
    name=request.POST.get('name')

    mydata={
        "name":name
    }
    mytba.insert_one(mydata)
    print("Data Added")
    return redirect('/',data)
    
    