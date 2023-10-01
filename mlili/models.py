from django.db import models

# Create your models here.
""" class Question(models.Model):
    text=models.CharField(max_length=200,blank=True)
    time=models.DateTimeField("Date")
class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200) """

class Program(models.Model):
    task=models.CharField(max_length=200,blank=True)
    time_line=models.TimeField("time line")
    time_line_end=models.TimeField("time_line_end")
     
   
    
