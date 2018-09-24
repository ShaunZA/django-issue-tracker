from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import Ticket, Comment


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'ticket_type']
        labels = {
            'ticket_type': _('Ticket Type'),
        }
        help_texts = {
            'ticket_type': _('Please note: Feature request will cost €30')
        }


class CommentForm(ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='')
    class Meta:
        model = Comment
        fields = ['text']