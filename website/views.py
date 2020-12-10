from django.shortcuts import render, HttpResponse
from .models import Card, ContactForm

def index(request):
    return render(request, 'website/index.html')

def board(request):
    return render(request, 'website/board.html')

def contactUs(request):
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        if (not(name and email and phone and message) or name.strip() == ''):
            context['error'] = "Form cannot submitted for insufficient information!"
            return render(request, 'website/contact.html', context)
        ContactForm.objects.create(
            name=name.strip(),
            email=email,
            phone=phone,
            message=message
        )
        context['success'] = "Thanks for Submitting the form 👍"
        return render(request, 'website/contact.html', context)
    return render(request, 'website/contact.html')

def campaigns(request):
    card = Card.objects.get(card_name="Campaigns")
    context = {'card': card}
    return render(request, 'website/campaigns.html', context)

def internship(request):
    card = Card.objects.get(card_name="Internships")
    context = {'card': card}
    return render(request, 'website/internship.html', context)

def mental(request):
    card = Card.objects.get(card_name="Mental")
    context = {'card': card}
    return render(request, 'website/mental.html', context)

def webinar(request):
    card = Card.objects.get(card_name="Webinar")
    context = {'card': card}
    return render(request, 'website/webinar.html', context)
