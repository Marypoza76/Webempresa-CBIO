from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .forms import ContactForm

def home(request):
    return render(request, 'cbiolab/base.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'cbiolab/register.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'cbiolab/contact.html', {'form': form})

def login(request):
    return render(request, 'cbiolab/login.html')

def services(request):
    return render(request, 'cbiolab/services.html')

