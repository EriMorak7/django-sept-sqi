from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ask(request):
    return render(request, "pages/ask.html")

