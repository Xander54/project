from typing import Any
from django.conf import UserSettingsHolder
from django.db import models
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils import timezone
import datetime
from django.db.models.query import QuerySet
from django.views.generic import View
from .models import Program
from django.views.generic import DetailView,ListView,TemplateView
from django.contrib.auth import login,authenticate
 
import os





# Create your views here.
class Index(TemplateView):
    template_name="location/time_line.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list'] = Program.objects.order_by('-id')
        return context
class Data(ListView):
    template_name="location/index.html"
    message="pls don't less empty feild ?"
    def post(self,request):
        task=request.POST["task"]
        time_line=request.POST["time_line"]
        time_line_end=request.POST["time_line_end"]
        if task!="":
            try:
                tasks=Program(task=task,time_line=time_line,time_line_end=time_line_end)
                tasks.save()   
            except:
                
                return render (request,"location/index.html",{"message":self.message})
            return redirect("time_line")
        else:
            return render (request,"location/index.html",{"message":self.message})
    def get_queryset(self):
        return Program.objects.all()

class Userpage(ListView):
    template_name="location/user.html"
    #context_object_name="questions"
    """ def get(self,request):
        time=timezone.now()
        #return render(request,self.template_name,{"time":time})
        return render(request,self.template_name,{"time":time}) """
    """ def post(self,request):
        question=request.POST['question']
        choice1=request.POST['choice1']
        choice2=request.POST['choice2']
        choice3=request.POST['choice3']
        p=Question(text=question,time=timezone.now())
        p.save()
        p.choice_set.all()
        p.choice_set.create(choice_text=choice1)
        p.choice_set.create(choice_text=choice2)
        p.choice_set.create(choice_text=choice3)
        
        
        return render(request,self.template_name)
        def post(self,request):
        usename=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if
    def get_queryset(self):
        return Question.objects.order_by("-time")[:10] """
    

        
    
        
    
    