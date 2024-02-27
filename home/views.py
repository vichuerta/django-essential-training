from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# every time this function recieves a request, it will return this http response

# how does it know when to run? URLs file!
def home(request):
    return render(request, 'home/welcome.html', {'today': datetime.today()})