from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from cusxstuff.settings import STRIPE_KEY, YOUR_DOMAIN

import stripe
stripe.api_key = STRIPE_KEY


""" session stripe """


class CreateSession(APIView):
    def post(self, request, *args, **kwargs):
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'unit_amount': 2000,
                            'product_data': {
                                'name': 'Stubborn Attachments',
                                'images': ['https://i.imgur.com/EHyR2nP.png'],
                            },
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success.html',
                cancel_url=YOUR_DOMAIN + '/cancel.html',
            )
            return Response({'id': checkout_session.id})
        except Exception as e:
            return Response(error=str(e), status=status.HTTP_403_FORBIDDEN)
