import stripe
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Item

stripe.api_key = 'sk_test_51M6SN1AEAFr0xNHsvxfy6mGIkxqOKVugsPWU3WFBthL68jNC0cC1GX5R9q3YbwKy6AXZ8OzEC5C3lCYWwYHJy45b00vDxYjpbM'
def buy(request, pk):
    item_id = pk
    item = Item.objects.get(id=item_id)
    YOUR_DOMAIN = "http://127.0.0.1:8000"
    checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": item.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
    
    return JsonResponse({
            'id': checkout_session.id
        })

def success(request):
    return HttpResponse('Оплата прошла успешно')

