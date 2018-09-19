from django import forms
from django.forms import ModelForm
from .models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'ticket_type', 'screenshot']