from django.shortcuts import render
from app.forms import *

# Create your views here.

def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
     WFO=WebpageForm()
     d={'WFO':WFO}
     if request.method=='POST':
         WFDO=WebpageForm(request.POST)
         if WFDO.is_valid():
             WFDO.save()

     return render(request,'insert_webpage.html',d)


def insert_accessrecords(request):
     AFO=AccessRecordsForm()
     d={'AFO':AFO}
     if request.method=='POST':
         AFDO=WebpageForm(request.POST)
         if AFDO.is_valid():
             AFDO.save()
     return render(request,'insert_accessrecords.html',d)



