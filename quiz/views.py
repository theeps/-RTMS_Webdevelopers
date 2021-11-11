from django.shortcuts import render
#from django.http import HttpResponse
#from quiz.models import Exam

# Create your views here.
#def home(request):
    #return HttpResponse("Hello")

#def home(request):
    #exam = Exam.objects.all()
    #return render(request,"home.html",{"exam":exam})

    from django.db import models


# Create your models here.
class QuesModel(models.Model):
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question
