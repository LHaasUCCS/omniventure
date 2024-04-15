from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from django.views import generic
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
import requests


# Create your views here.
def index(request):

    return render( request, 'omniventure_app/index.html')

def member_edit(request):

    return render( request, 'omniventure_app/member_edit_message.html')

class member_list(generic.ListView):
    model = Member

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Pass the currently authenticated user to the template
        return context

class member_detail(generic.DetailView):
    model = Member

class member_create(LoginRequiredMixin, generic.CreateView):
    model = Member
    form_class = member_form
    success_url = reverse_lazy('member_edit_message')


    def form_valid(self, form):
        # Assign the current logged-in user to the user field of the Member instance
        form.instance.user = self.request.user
        return super().form_valid(form)

class member_delete(LoginRequiredMixin, generic.DeleteView):
    model = Member
    success_url = reverse_lazy('member_list')

    def get_object(self, queryset=None):
        member = super().get_object(queryset)

        if not member.delete(self.request.user):
            return redirect('user_login')


class member_update(LoginRequiredMixin, generic.UpdateView):
    model = Member
    form_class = member_form
    success_url = reverse_lazy('member_edit_message')


    def get_object(self, queryset=None):
        # Get the member object
        member = super().get_object(queryset)

        # Check if the current user has permission to edit the member
        # this produces an error page if not logged in. Can't get
        # to work how I want, moving on. Still prevents non owners
        # from accessing update so.... yeah. Also buttons are hidden
        # so only malicious actors can access this page by URL access,
        # but it's still broken.
        if not member.can_edit(self.request.user):
            return redirect('user_login') 
        
        return member


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  
    else:
        form = UserCreationForm()
    return render(request, 'omniventure_app/register.html', {'form': form})        
    

def add_character(request, pk):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            # Fetch member instance based on the provided primary key (pk)
            # Assuming your Member model is imported and pk refers to the member's primary key
            member = Member.objects.get(pk=pk)

            # Obtain character_id from the form data
            character_id = form.cleaned_data['character_id']

            # Fetch character data from FFXIVCollect API
            url = f"https://ffxivcollect.com/api/characters/{character_id}/"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()

                # Extract fields from the API response
                name = data.get('name')
                server = data.get('server')
                data_center = data.get('data_center')
                portrait = data.get('portrait')
                avatar = data.get('avatar')

                # Create a new instance of Character model with API data and form data
                character = Character(
                    character_id=character_id,
                    member=member,
                    name=name,
                    server=server,
                    data_center=data_center,
                    portrait=portrait,
                    avatar=avatar
                )
                character.save()

                # Redirect to a success page or render a success template
                return redirect('member_detail', pk=member.pk)
            else:
                # Handle API request failure (e.g., API error or character not found)
                # You can add appropriate error handling here
                pass
    else:
        form = CharacterForm()
    return render(request, 'omniventure_app/add_character.html', {'form': form})

class delete_character(generic.DeleteView):
    model = Character
    success_url = reverse_lazy('member_detail')

    def get_success_url(self):
        return reverse_lazy('member_detail')
    
class character_detail(generic.DetailView):
    model = Character

class edit_character(generic.UpdateView):
    model = Character
    fields = ['character_id', 'background', 'personality', 'pronouns']
    

