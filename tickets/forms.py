from django import forms
from django.forms import ModelForm
from .models import Ticket, Comment


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'ticket_type']


class CommentForm(ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = Comment
        fields = ['text']