from django.shortcuts import render

from polls.models import Classroom, Student


def index(request):
    classroom = Classroom.objects.all()
    context = {
        'data': classroom,
    }
    return render(request, 'polls/index.html', context)


def get_student(request, classroom_id):
    classroom = Classroom.objects.get(id=classroom_id)
    student = Student.objects.filter(classroom=classroom)
    context = {
        'data': student
    }
    return render(request, 'polls/detail.html', context)
