from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required
from djstripe.models import Customer, Card, Plan
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger('django')


@login_required
def profile_view(request):
    (st_customer, _) = Customer.get_or_create(request.user)

    if st_customer.default_source:
        default_source = st_customer.default_source
    else:
        default_source = None

    context = {
        'user': request.user,
        'customer': st_customer,
        'default_source': default_source,
        'sources': st_customer.sources.all(),
    }
    return render(request, 'accountpage/profile.html', context)


@login_required
def add_card_view(request):
    if request.method == 'GET':
        context = {

        }
        return render(request, 'accountpage/add_card.html', context)
    elif request.method == 'POST':
        (st_customer, _) = Customer.get_or_create(request.user)
        res = st_customer.add_card(request.POST.get('stripe-token'))
        return redirect('/accounts/profile')


@login_required
def remove_card_view(request, card_id = ''):
    if card_id == '':
        return redirect('/accounts/profile')

    card = Card.objects.get(stripe_id=card_id)

    if card.customer.subscriber != request.user:
        return redirect('/accounts/profile')

    card.remove()
    return redirect('/accounts/profile')

@login_required
def make_default_card_view(request, card_id = ''):
    if card_id == '':
        return redirect('/accounts/profile')

    card = Card.objects.get(stripe_id=card_id)

    if not (card.customer.subscriber == request.user):
        logger.debug('Not your card')
        return redirect('/accounts/profile')

    card.customer.default_source = card
    card.customer.save()
    return redirect('/accounts/profile')

@login_required
def subscribe(request):
    (plan, _) = Plan.get_or_create(stripe_id='developer',
                       name='Developer Licence',
                       amount=10.00,
                       currency='USD',
                       interval='year',
                       interval_count='1')

    (customer, _) = Customer.get_or_create(request.user)

    if not customer.default_source:
        return redirect('/accounts/add_card')

    customer.subscribe(plan)

    return redirect('/accounts/profile')
