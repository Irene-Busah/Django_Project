from django.http import HttpResponse
from django.views.generic import ListView


# Create your views here.
def index(response):
    return HttpResponse("Hello World!")


