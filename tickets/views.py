from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Ticket
from .forms import TicketForm


# Create your views here.
def all_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, "tickets.html", {"tickets": tickets})


def one_ticket(request, ticket_id):
    tickets = Ticket.objects.filter(id=ticket_id)
    return render(request, "ticket.html", {"tickets": tickets})
    
@login_required
def create_ticket(request):
    form = TicketForm(request.POST, request.FILES or None)
    
    if request.method == 'POST':
        # If Feature created - go to payment
        if form.is_valid() and 'feature' in request.POST['ticket_type']:
            messages.success(request, "You have successfully created a new Feature ticket.")
            return redirect(reverse('index'))
        # If Bug created - Do this
        elif form.is_valid():
            form = form.save(commit=False)
            form.date_added = timezone.now()
            form.created_by = request.user.username
            form.save()
            messages.success(request, "You have successfully created a new Bug ticket.")
            return redirect(reverse('index'))

    return render(request, 'create.html', {'form': form})
    
