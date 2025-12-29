from django.http import HttpResponse
from django.shortcuts import render
import datetime

def test(request):
    print("test function called!")
    return HttpResponse("<h1>Test function called</h1>")  # Fixed typo

def home(request):
    print("home function called!")
    nums = [1,2,3,4,5,6,7,8]
    data = {'nums':nums}
    return render(request, 'index.html',data)  # Empty context is optional

def about(request):
    print("about function called!")
    return render(request, 'about.html')

def service(request):
    print("service function called!")
    return render(request, 'service.html')

def contact(request):
    print("contact function called!")  # Fixed typo
    return render(request, 'contact.html')

def current_date_time(request):
    now = datetime.datetime.now()
    formatted = now.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse(f"<h1>Current Date & Time: {formatted}</h1>")
