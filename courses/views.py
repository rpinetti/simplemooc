from django.shortcuts import render, get_object_or_404

from .models import Course


# Create your views here.
def courses(request):
    template_name = 'courses/index.html'

    courses_list = Course.objects.all()
    context = {
        'courses': courses_list
    }

    return render(request, template_name, context)


def details(request, slug):
    template_name = 'courses/details.html'

    course = get_object_or_404(Course, slug=slug)  # Executa a query e exibe a pagina 404 quando o registro não existir
    # course = Course.objects.get(pk=pk)
    context = {
        'course': course
    }

    return render(request, template_name, context)
