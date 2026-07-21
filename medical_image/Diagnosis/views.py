from django.shortcuts import render,redirect,get_object_or_404
from django.conf import settings
#from .models import contact,crop_recommend,CropDetail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login as ln,logout
from django.contrib import messages
import joblib,os

def index(request):
    return render(request,'Diagnosis/index.html')

def about(request):
    return render(request,'Diagnosis/about.html')

def home(request):
    return render(request,'Diagnosis/home.html')

def terms(request):
    return render(request,'Diagnosis/terms.html')

def result(request):
    return render(request,'Diagnosis/result.html')

def dashboard(request):
    return render(request,'Diagnosis/dashboard.html')

def diagnosis(request):
    pass

def services(request):
    return render(request,'Diagnosis/services.html')

def contact(request):
    return render(request,'Diagnosis/contact.html')

def faq(request):
    return render(request,'Diagnosis/faq.html')

def history(request):
    return render(request,'Diagnosis/history.html')

def documentation(request):
    return render(request,'Diagnosis/documentation.html')

def metrics(request):
    return render(request,'Diagnosis/metrics.html')

def modalities(request):
    return render(request,'Diagnosis/modalities.html')

def pricing(request):
    return render(request,'Diagnosis/pricing.html')

def privacy(request):
    return render(request,'Diagnosis/privacy.html')

def register(request):
    return render(request,'Diagnosis/register.html')

def report(request):
    return render(request,'Diagnosis/report.html')

def reports(request):
    return render(request,'Diagnosis/reports.html')

def research(request):
    return render(request,'Diagnosis/research.html')

def support(request):
    return render(request,'Diagnosis/support.html')

def team(request):
    return render(request,'Diagnosis/team.html')


def user_login(request):
    return render(request,'Diagnosis/login.html')


