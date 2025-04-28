from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Lego, Wishlist
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect ('lego-index')
        else:
            error_message = 'Invalid login credentials - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

@login_required
def about(request):
    about_details = 'Do you have way too many legos? Same. Keep up with all the sets you own and those on your wishlist with Lego Collector!'
    return render(request, 'about.html', {
        'about': about_details
    })

@login_required
def lego_index(request):
    legos = Lego.objects.all()
    return render(request, 'legos/index.html', {'legos': legos})

@login_required
def lego(request, lego_id):
    lego = Lego.objects.get(id=lego_id)
    return render(request, 'legos/detail.html', {
        'lego': lego,
    })

class LegoCreate(LoginRequiredMixin, CreateView):
    model = Lego
    fields = ['name', 'category', 'description', 'pieces']

    success_url = '/legos/'

    # def form_valid(self, form):
    #     # Assign the logged in user (self.request.user)
    # form.instance.user = self.request.user  # form.instance is the cat
    #     # Let the CreateView do its job as usual
    # return super().form_valid(form)

class LegoUpdate(LoginRequiredMixin, UpdateView):
    model = Lego
    fields = '__all__'

class LegoDelete(LoginRequiredMixin, DeleteView):
    model = Lego
    success_url = '/legos/'

class WishlistCreate(LoginRequiredMixin, CreateView):
    model = Wishlist
    fields = '__all__'

    success_url = '/wishlist/'

class WishlistList(LoginRequiredMixin, ListView):
    model = Wishlist

class WishlistDetail(LoginRequiredMixin, DetailView):
    model = Wishlist

class WishlistUpdate(LoginRequiredMixin, UpdateView):
    model = Wishlist
    fields = ['name', 'category']

class WishlistDelete(LoginRequiredMixin, DeleteView):
    model = Wishlist
    success_url = '/wishlist/'
# remember to add login required mixin