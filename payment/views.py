from django.shortcuts import render, redirect
from issue_tracker import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Feature
from tickets.forms import TicketForm
from django.contrib import messages
import stripe

stripe.api_key = settings.STRIPE_SECRET

# Create your views here.
def payment_form(request):
    context = { "stripe_key": settings.STRIPE_PUBLISHABLE }
    return render(request, "payment.html", context)


def checkout(request):
    form = TicketForm(request.POST)
    new_feature = Feature(
        name = "One Feature"
    )

    if request.method == "POST":
        token = request.POST.get("stripeToken")

    try:
        charge  = stripe.Charge.create(
            amount = 3000,
            currency = "eur",
            source = token,
            description = "One Feature Added - {0}".format(request.user.username)
        )

        new_feature.charge_id   = charge.id

    except stripe.error.CardError as ce:
        return False, ce

    else:
        new_feature.save()
        return redirect('create_feature')
    
    return redirect('create_feature')