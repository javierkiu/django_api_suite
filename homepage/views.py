from django.shortcuts import render

def index(request):
    # return HttpResponse("¡Bienvenido a la aplicación Django!")
    return render(request, 'homepage/index.html')