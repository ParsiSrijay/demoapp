from django.shortcuts import render
from organizations.models import Addpolicy1
# Create your views here.

def addpolicy(request):

    if request.method=='POST':
        name=request.POST['pol_name']
        desc=request.POST['pol_des']
        q1=request.POST['ques1']
        q2=request.POST['ques2']
        q3=request.POST['ques3']
        q4=request.POST['ques4']
        q5=request.POST['ques5']
        a=Addpolicy1(Policyname=name,Description=desc,Question1=q1,Question2=q2,Question3=q3,Question4=q4,Question5=q5)
        a.save()
        return render(request,'addpolicy.html',{'content':"policy Added"})
    else:
        return render(request,'addpolicy.html')
