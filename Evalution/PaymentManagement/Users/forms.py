from django import forms
from .models import Subscription

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['service_user', 'service', 'amount']
        widegets = {
            'service_user': forms.Select(),
            'service': forms.Select(),
            'amount': forms.NumberInput()
        }







