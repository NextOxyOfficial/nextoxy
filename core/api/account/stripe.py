import stripe

def makeStripePayment(invoice, value1 = '', value2='', value3=''):
    stripe.api_key = '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'
    # stripe.api_key = 'sk_test_51MZyl0COzgULzFM3l86TaSHESsKJj5x59N0ii219AiHMC3otWAM9gcxkdgSo1LQsoObk6KKiusQlcQCe6omDbPET00BK9U0yzn'
    domain_url = 'https://nextoxy.com'
    stripe_price = int(str(invoice.amount).replace('.', ''))
    checkout_session = stripe.checkout.Session.create(
        success_url=domain_url + invoice.redirect,
        cancel_url=domain_url + invoice.redirect,
        client_reference_id = str(invoice.id),
        payment_method_types=['card'],
        mode='payment',
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Stubborn Attachments',
                        'images': ['https://i.imgur.com/EHyR2nP.png'],
                    },
                    'unit_amount': stripe_price,
                    # 'recurring': {"interval": "month"},
                },
                'quantity': 1,
            },
        ]
    )
    return checkout_session