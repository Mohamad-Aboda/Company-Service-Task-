from django.shortcuts import render
from django.http import HttpResponse, request


from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person

def lead(request):
    return render(request,'lead.html')


def screen2(request):
    return render(request, 'screen2.html')

def screen3(request):
    return render(request, 'screen3.html')



class PersonListView(ListView):
    model = Person
    context_object_name = 'people'

class PersonCreateView(CreateView):
    model = Person
    fields = ('first_name', 'last_name', 'email', 'phone', 'company_name', 'objective', 'more_details_description')
    success_url = reverse_lazy('person_changelist')

class PersonUpdateView(UpdateView):
    model = Person
    fields = ('first_name', 'last_name', 'email', 'phone', 'company_name', 'objective', 'more_details_description')    
    success_url = reverse_lazy('person_changelist')
