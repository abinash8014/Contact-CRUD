from django.shortcuts import render
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    un = request.session.get('username')
    if un:
        UO = User.objects.get(username=un)
        d = {'UO':UO}
        return render(request,'home.html',d)
    return render(request,'home.html')

def register(request):
    EUFO = UserForm()
    d = {'EUFO':EUFO}
    if request.method == 'POST':
        UFDO = UserForm(request.POST)
        if UFDO.is_valid():
            pw = UFDO.cleaned_data.get('password')
            MUFDO = UFDO.save(commit=False)
            MUFDO.set_password(pw)
            MUFDO.save()
            return HttpResponseRedirect(reverse('user_login'))
        return HttpResponse('Invalid Data')
    return render(request,'register.html',d)

def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('un')  
        pw = request.POST.get('pw')
        print(un)
        print(pw)
        AUO = authenticate(username=un,password=pw)
        print(AUO)
        if AUO:
            login(request,AUO)
            request.session['username']= un
            return HttpResponseRedirect(reverse('home'))
        return HttpResponse('Invalid creds')
    return render(request,'user_login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
    
def create_contact(request):
    un = request.session.get('username')
    if un:
        if request.method == 'POST' and request.FILES:
            UO=User.objects.get(username=un)
            CFDO = ContactForm(request.POST,request.FILES)
            if CFDO.is_valid():
                MCFDO = CFDO.save(commit=False)
                MCFDO.username = UO
                MCFDO.save()
                return HttpResponseRedirect(reverse('home'))
            return HttpResponse('Invalid Data')
        ECFO = ContactForm()
        d = {'ECFO':ECFO}
        return render(request,'create_contact.html',d)
    return HttpResponse('username not found')

def display(request,pk):
    un = request.session.get('username')
    if un:
        CO = Contact.objects.get(pk=pk)
        d  =  {'CO':CO}
        return render(request,'display.html',d)
    return HttpResponseRedirect(reverse('user_login'))

def update(request,pk):
    un = request.session.get('username')
    if un:
        CO = Contact.objects.get(pk=pk)
        d = {"CO":CO}
        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            add = request.POST.get('add')
            CO.name = name
            CO.email = email
            CO.add = add
            CO.save()
            return HttpResponseRedirect(reverse('home'))
        return render(request,'update.html',d)
    return HttpResponseRedirect(reverse('user_login'))

def delete(request,pk):
    un = request.session.get('username')
    if un:
        CO = Contact.objects.get(pk=pk)
        CO.delete()
        return HttpResponseRedirect(reverse('home'))
    return HttpResponseRedirect(reverse('user_login'))
    
def search(request):
    if request.method == 'POST':
        pk = request.POST.get('search')
        print(pk)
        CO = Contact.objects.get(pk=pk)
        d = {'CO':CO}
    return render(request,'display.html',d)