
import requests
import json
def makePaypalPayment(invoice, currency='USD', return_url="/account/billing", cancel_url="/account/billing"):
    # Set up PayPal API credentials
    client_id = "AUnIIRCkAM1wbS55t4EDvQpgE1WpsyO_ApJyrbWxpsleFcKGtveUnq03_y0TuT6qBC1ToVF3AjcOjfen"
    secret = "ENT0qLr_mAc0bemaYUCy-t2aJmd44AydHgi3pwPkw3UHCJy60UazmCSDbVtQnSDi-940LbdT0najxigQ"
    base_url = "https://api.sandbox.paypal.com"
    # base_url = "https://api.paypal.com"
    # Set up API endpoints
    token_url = base_url + '/v1/oauth2/token'
    payment_url = base_url + '/v1/payments/payment'

    # Request an access token
    token_payload = {'grant_type': 'client_credentials'}
    token_headers = {'Accept': 'application/json', 'Accept-Language': 'en_US'}
    token_response = requests.post(token_url, auth=(client_id, secret), data=token_payload, headers=token_headers)

    if token_response.status_code != 200:
        return False,"Failed to authenticate with PayPal API",None

    access_token = token_response.json()['access_token']

    # Create payment payload
    payment_payload = {
        'intent': 'sale',
        'payer': {'payment_method': 'paypal'},
        'transactions': [{
            'amount': {'total': str(invoice.amount), 'currency': currency},
            'description': 'Nextoxy Service'
        }],
        'redirect_urls': {
            'return_url': return_url,
            'cancel_url': cancel_url
        }
    }

    # Create payment request
    payment_headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }

    payment_response = requests.post(payment_url, data=json.dumps(payment_payload), headers=payment_headers)
    # print(payment_response.text)
    if payment_response.status_code != 201:
        return False , 'Failed to create PayPal payment.',None

    payment_id = payment_response.json()['id']
    approval_url = next(link['href'] for link in payment_response.json()['links'] if link['rel'] == 'approval_url')

    return True,payment_id, approval_url
