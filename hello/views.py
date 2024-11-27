from django.http import HttpResponse

def hello_view(request, name):
    return HttpResponse(f"Hello, {name}!")

def confirmation_view(request):
    return HttpResponse("it worked!")