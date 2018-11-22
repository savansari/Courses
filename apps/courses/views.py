from django.shortcuts import render,redirect
from .models import Course
from django.contrib import messages
# Create your views here.
def index(req):
    courses_list=Course.objects.LoadAll()
    context={
        'objects':courses_list
    }
    return render(req,'courses/index.html',context)
def create(req):
    errors=[]
    errors=Course.objects.validate(req.POST)
    if len(errors)>0:
        for error in errors:
            messages.error(req,error)
    else:
        course=Course.objects.create_course(req.POST)
        req.session['course_id']=course.id
        print("here")
        courses_list=Course.objects.LoadAll()
        context={
            'objects':courses_list
        }
        return render(req,'courses/index.html',context)
    return redirect('/')
def delete(req,id):
    Course.objects.delete(id)
    return redirect('/')
def confirm(req,id):
    info=Course.objects.Load(id)
    context={
        'objects':info
    }
    return render(req,'courses/confirm.html',context)
     