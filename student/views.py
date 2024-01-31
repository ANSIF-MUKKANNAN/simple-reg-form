from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from .models import regt
from .forms import AddForm
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
# Create your views here.

def insert(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        gender=request.POST.get('gender')
        
        regt(firstname=firstname,lastname=lastname,email=email,phone=phone,password=password,gender=gender).save()
    return render(request,'registration.html')

def view(request):
    cr=regt.objects.all()
    return render(request,'views.html',{'cr':cr})

def detailview(request,pk):
     cr=regt.objects.get(id = pk)
     return render(request,'detailedview.html',{'cm':cr})

def update(request,pk):
    cr = regt.objects.get(id=pk)
    form1 =AddForm(instance=cr)
    if request.method =="POST":
        form1 = AddForm(request.POST,instance=cr)
        if form1.is_valid:
            form1.save()
        return redirect("views")
    return render(request,"update.html",{'form1':form1})

def delete(request,pk):
    cr=regt.objects.get(id = pk)
    cr.delete()
    return redirect('views')

def login(request):
    return render(request,'login.html')

def userlogin(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        cr=regt.objects.filter(email=email, password=password)
        if cr:
            user_details=regt.objects.get(email=email, password=password)

            id=user_details.id
            firstname=user_details.firstname
            lastname=user_details.lastname
            email=user_details.email

            request.session['id']=id
            request.session['firstname']=firstname
            request.session['lastname']=lastname
            request.session['email']=email

            return redirect('display')
        else:
            err="invalid username or password"
            return HttpResponse(render(request,'login.html',{'err':err}))
    else:
        return render(request,'views.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

def adminlogin(request):
    return render(request,'adminlogin.html')


def alogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('adminlogin')
    else:
        return render(request,'adminlogin.html')
