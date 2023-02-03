from django.shortcuts import render, get_object_or_404

from .forms import ContactCourse
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
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form.send_email(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['course'] = course
    context['form'] = form
    return render(request, template_name, context)
