import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

def buy_item(request, id):
    item = get_object_or_404(Item, id=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': "rub",
                'product_data': {
                    'name': item.name,
                    'description': item.description,
                },
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri('/success/'),
        cancel_url=request.build_absolute_uri('/cancel'),
    )
    return JsonResponse({'sessionId': session.id})

def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'item.html', {'item': item, 'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})


def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})


def success(request):
    return render(request, 'success.html')

def cancel(request):
    return render(request, 'cancel.html')

