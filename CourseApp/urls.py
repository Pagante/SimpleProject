from django.urls import path
from . import views

urlpatterns = [
    path('',views.course, name='Courses'),
    path('<int:id>', views.course_details, name='course_details'),
]