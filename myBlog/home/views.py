from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
def home(request):
    return render(request, 'home/home.html')

def contact(request):
    if (request.method == "POST"):
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        query = request.POST['query']

        if len(name)<3 or len(email)<15 or len(phone)<10:
            messages.error(request, "Oops! Please enter the correct details.")
        else:
            contact = Contact(name=name, phone=phone, email=email, query=query)
            contact.save()
            messages.success(request, 'Success!!! Thanks '+name+" for submitting your query." )

    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')