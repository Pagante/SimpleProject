from django.shortcuts import render, get_object_or_404
from .models import CourseDetail
from PortFolio .models import Course

# Create your views here.
def course(request):
    all_courses = Course.objects.all()
    data = {
        'all_courses':all_courses
    }
    return render(request, 'CourseApp/course.html', data)

def course_details(request, id):
    feature_courses = get_object_or_404(CourseDetail, pk=id)
    data = {
        'feature_courses':feature_courses
    }
    return render(request, 'CourseApp/course_details.html',data)