from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from django.views import generic
#from .forms import *
from django.shortcuts import redirect
# Create your views here.
def index(request):

    return render( request, 'omniventure_app/index.html')

class member_list(generic.ListView):
    model = Member

class member_detail(generic.DetailView):
    model = Member
