from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import  login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import BiodataModel

from .forms import CreateBiodata




#signup
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('main')
        else:
            messages.info(request,'Username or Password is incorrect')

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('index')

#Home
def index(request):
    return render(request, 'index.html', {})


def blog(request):
   return render(request, 'blog.html', {})

def myprofile(request):
   return render(request, 'myprofile.html', {})  

def profile(request):
   return render(request, 'profile.html', {})  


def news(request):
    return render(request, 'news.html', {})

def pricing_view(request):
    return render(request, 'pricing.html', {})

@login_required(login_url='login')
def mainPage(request):
    return render(request, 'main.html', {})


def biodata_list(request):
    biodatalist = BiodataModel.objects.all()
    return render(request, 'biodata_list.html', {'biodatalist': biodatalist})



def biodata_detail(request, BiodataModel_id):
    biodatadetail = BiodataModel.objects.get(pk=BiodataModel_id)
    return render(request, 'biodata_detail.html', {'biodatadetail': biodatadetail})


@login_required(login_url='login')
def biodata_create(request):
    submitted = False
    if request.method == "POST":
        form = CreateBiodata(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/createbiodata?submitted=True')
    else:
        form = CreateBiodata
        if 'submitted' in  request.GET:
            submitted =  True  
    return render(request, 'biodata_create.html', {'form': form, 'submitted':submitted})


@login_required(login_url='login')
def search_bio(request):
    if request.method == "POST":
        searched = request.POST['searched']
        bio = BiodataModel.objects.filter(gender__contains=searched)
        
        return render(request, 'search_bio.html', {'searched': searched, 'bio': bio})
    
    else:
        return render(request, 'search_bio.html', {})



    
