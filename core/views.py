from django.shortcuts import render


# Create your views here.
def home(request):
    # renderiza o arquivo home.html localizado na pasta template
    return render(request, 'home.html', {'usuario': 'Roberto'})


def contact(request):
    return render(request, 'contact.html')
