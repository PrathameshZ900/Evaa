from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import ServiceUser, Service, Subscription
from .forms import SubscriptionForm



class UserListView(ListView):
    model = ServiceUser
    template_name = 'Users/serviceuser_list.html'


class UserDetailView(DetailView):
    model = ServiceUser
    template_name = "Users/user_detail.html"
    context_object_name = "user"



class ServiceListView(ListView):
    model = Service
    template_name = 'services.html'  # the name of your template file
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'Users/service_detail.html'

class CreateSubscriptionView(CreateView):
    model = Subscription
    form_class =  SubscriptionForm
    template_name = 'Users/create_subscription.html'
    success_url = reverse_lazy('user_list')





