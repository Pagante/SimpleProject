from django.shortcuts import render
from .models import Course

# Create your views here.
def index(request):
    courses = Course.objects.all()
    data = {
        'courses' : courses
    }
    return render(request,'PortFolio/index.html' ,data)
