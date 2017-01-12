from django.shortcuts import render

from lesson.models import Lesson


def lessons(request):
    lessons = Lesson.objects.all()
    context = {
        'lessons' : lessons
    }

    return render(request, 'lesson/lesson.html' , context)
