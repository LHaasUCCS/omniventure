from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from django.views import generic
from django.shortcuts import redirect
from .forms import *

# Create your views here.
def index(request):

    return render( request, 'omniventure_app/index.html')

def member_edit(request):

    return render( request, 'omniventure_app/member_edit_message.html')

class member_list(generic.ListView):
    model = Member

class member_detail(generic.DetailView):
    model = Member

class member_create(generic.CreateView):
    model = Member
    form_class = member_form
    success_url = reverse_lazy('member_edit_message') 

class member_delete(generic.DeleteView):
    model = Member
    success_url = reverse_lazy('member_list') 

class member_update(generic.UpdateView):
    model = Member
    form_class = member_form
    success_url = reverse_lazy('member_edit_message')
        
    
