from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student
# Create your views here.
def index(request):
    return render(request, 'students/index.html', {
        'students': Student.objects.all(),
    })

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(request, student)