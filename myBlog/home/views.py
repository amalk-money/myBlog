from django.shortcuts import render, HttpResponse
from home.models import Contact
def home(request):
    return render(request, 'home/home.html')

def contact(request):
    if (request.method == "POST"):
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        query = request.POST['query']
        contact = Contact(name=name, phone=phone, email=email, query=query)
        contact.save()
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')