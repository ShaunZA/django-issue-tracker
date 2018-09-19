from django.shortcuts import render
from django.db.models import Q
from tickets.models import Ticket

# Create your views here.

def do_search(request):
    tickets = Ticket.objects.filter(Q(title__icontains=request.GET['q']) | Q(created_by__icontains=request.GET['q']) | Q(priority__icontains=request.GET['q']) | Q(ticket_type__icontains=request.GET['q']) | Q(description__icontains=request.GET['q']))
    return render(request, 'tickets.html', {"tickets": tickets})