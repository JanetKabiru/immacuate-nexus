from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def events(request):
    return render(request,'events.html')

def contacts(request):
    return render(request,'contacts.html')

def courses(request):
    return render(request,'courses.html')

def admissions(request):
    return render(request,'admissions.html')

def about(request):
    return render(request,'about.html')