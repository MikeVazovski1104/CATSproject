from django.http import HttpResponse

def hello_cats(request):
    return HttpResponse("Hello from cats")