from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views import View
from .models import ServiceUser, Service, Subscription
from .forms import SubscriptionForm


class UserListView(ListView):
    model = ServiceUser
    template_name = 'Users/serviceuser_list.html'

class UserDetailView(DetailView):
    model = ServiceUser

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        return render(request, 'Users/user_detail.html', {'user': user})





class ServiceListView(ListView):
    model = Service
    template_name = 'services.html'  # the name of your template file
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'Users/service_detail.html'

class CreateSubscriptionView(View):
    template_name = 'Users/create_subscription.html'  # Adjust path as necessary

    def get(self, request, *args, **kwargs):
        form = SubscriptionForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            # Process valid form data (save subscription, etc.)
            return redirect('success_url')  # Replace with your success URL
        return render(request, self.template_name, {'form': form})


