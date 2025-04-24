from django.shortcuts import render
from .models import Lego

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    about_details = 'Do you have way too many legos? Same. Keep up with all the sets you own and those on your wishlist with Lego Collector!'
    return render(request, 'about.html', {
        'about': about_details
    })

def lego_index(request):
    legos = Lego.objects.all()
    return render(request, 'legos/index.html', {'legos': legos})