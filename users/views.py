from django.shortcuts import render
from organizations.models import Addpolicy1
from .models import userresponse1
# Create your views here.
from django.db.models import Avg, Count, Min, Sum, Max
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def feedbackrequest(request):
    global Polname
    list_policies = Addpolicy1.objects.raw('SELECT  Policyname,id from organizations_Addpolicy1')
    l=[]
    for i in list_policies:
        l.append(i.Policyname)
    print(l)
    if(request.method=="POST"):
        if(request.POST["ADD"]=="ADD"):
            a=""
            b=""
            c=""
            d=""
            e=""
            q1 = Addpolicy1.objects.values('Question1', 'Question2', 'Question3', 'Question4', 'Question5').filter(
                Policyname=Polname)
            print(q1)
            for i in q1:
                print(i['Question1'],i['Question2'],i['Question3'],i['Question4'],i['Question5'])
                if (i['Question1']!=""):
                    a=request.POST[i['Question1']]
                if (i['Question2']!=""):
                    b=request.POST[i['Question2']]
                if (i['Question3']!=""):
                    c=request.POST[i['Question3']]
                if (i['Question4']!=""):
                    d=request.POST[i['Question4']]
                if (i['Question5']!=""):
                    e=request.POST[i['Question5']]
            u=userresponse1(Policyname=Polname,Question1=a,Question2=b,Question3=c,Question4=d,Question5=e)
            u.save()
            l3=[]
            for i in q1:
                dict={}
                if (i['Question1']!=""):
                    dict['q1']=i['Question1']
                    dict['ans1']=a
                if (i['Question2']!=""):
                    dict['q2'] = i['Question2']
                    dict['ans2'] = b
                if (i['Question3']!=""):
                    dict['q3'] = i['Question3']
                    dict['ans3'] = c
                if (i['Question4']!=""):
                    dict['q4'] = i['Question4']
                    dict['ans4'] = d
                if (i['Question5']!=""):
                    dict['q5'] = i['Question5']
                    dict['ans5'] = e
                l3.append(dict)
                print(l3)
            return render(request,'userfeedback.html',{'list3':l3})
        else:
            Polname= request.POST['pname']
            q1=Addpolicy1.objects.values('Question1','Question2','Question3','Question4','Question5').filter(Policyname=Polname)
            l2=[]
            for i in q1:
                if(i['Question1']!=""):
                    l2.append(i['Question1'])
                if(i['Question2']!=""):
                    l2.append(i['Question2'])
                if(i['Question3']!=""):
                    l2.append(i['Question3'])
                if(i['Question4']!=""):
                    l2.append(i['Question4'])
                if(i['Question5']!=""):
                    l2.append(i['Question5'])
            return render(request,'userfeedback1.html',{'list':l2})
    else:
        return render(request,'userfeedback1.html',{'list1':l})


def aggr(request):
    list_policies = Addpolicy1.objects.raw('SELECT  Policyname,id from organizations_Addpolicy1')
    l = []
    for i in list_policies:
        l.append(i.Policyname)
    print(l)
    if(request.method=="POST"):
        Polname= request.POST['pname']
        q1 = Addpolicy1.objects.values('Question1', 'Question2', 'Question3', 'Question4', 'Question5').filter(Policyname=Polname)
        print(q1)
        a1=userresponse1.objects.filter(Policyname=Polname).aggregate(p=Avg('Question1'),q=Avg('Question2'),r=Avg('Question3'),s=Avg('Question4'),t=Avg('Question5'))
        print(a1['p'],a1['q'])
        for i in q1:
            print(i['Question1'],i['Question2'],i['Question3'],i['Question4'],i['Question5'])
            if (i['Question1']!=""):
                a=i['Question1']
            if (i['Question2']!=""):
                b=i['Question2']
            if (i['Question3']!=""):
                c=i['Question3']
            if (i['Question4']!=""):
                d=i['Question4']
            if (i['Question5']!=""):
                e=i['Question5']
        l3=[]
        for i in q1:
            dict={}
            if (i['Question1']!=""):
                dict['q1']=i['Question1']
                dict['ans1']=a1['p']
            if (i['Question2']!=""):
                dict['q2'] = i['Question2']
                dict['ans2'] = a1['q']
            if (i['Question3']!=""):
                dict['q3'] = i['Question3']
                dict['ans3'] = a1['r']
            if (i['Question4']!=""):
                dict['q4'] = i['Question4']
                dict['ans4'] = a1['s']
            if (i['Question5']!=""):
                dict['q5'] = i['Question5']
                dict['ans5'] = a1['t']
            l3.append(dict)
        print(l3)
        return render(request,'userfeedback.html',{'list3':l3})
    else:
        return render(request,'userfeedback.html',{'list1':l})