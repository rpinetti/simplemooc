from django.shortcuts import render

from .models import Course


# Create your views here.
def courses(request):
    template_name = 'courses/index.html'

    courses_list = Course.objects.all()
    context = {
        'courses': courses_list
    }

    return render(request, template_name, context)
