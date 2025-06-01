import requests

# url = 'https://sandbox.shurjopayment.com/api/get_token'
# url2 = 'https://sandbox.shurjopayment.com/api/secret-pay'
# access = {
#     "username":"sp_sandbox",
#     "password":"pyyk97hu&6u6"
# }
url = 'https://engine.shurjopayment.com/api/get_token'
url2 = 'https://engine.shurjopayment.com/api/secret-pay'
access = {
    "username":"lyriczsoft",
    "password":"lyrikskdzprvz&ud"
}
def makeSpPayment(invoice, value1 = '', value2='', value3=''):
    print(invoice)
    domain_url = 'https://nextoxy.com'
    result  = requests.post(url, data=access)
    result = result.json()
    token = result['token']
    store_id = result['store_id']
    execute_url = result['execute_url']
    hed = {'Authorization': 'Bearer ' + token}

    data = {
        "token": token,
        "store_id": store_id,
        "prefix": "LST",
        "currency": "USD",
        "return_url": domain_url + '/account/sp/'+str(invoice.id),
        "cancel_url": domain_url + invoice.redirect,
        "amount": str(invoice.amount),
        "order_id": "order-"+str(invoice.id),
        "discsount_amount": "0",
        "disc_percent": "0",
        "client_ip": "118.179.34.243",
        "customer_name": invoice.account.billing_first_name +' '+ invoice.account.billing_last_name,
        "customer_phone": invoice.account.billing_phone_number,
        "customer_email": invoice.account.billing_email,
        "customer_address": invoice.account.billing_address,
        "customer_city": invoice.account.billing_city,
        "customer_state": invoice.account.billing_state,
        "customer_postcode": invoice.account.billing_zip_code,
        "customer_country": invoice.account.billing_country,
        'value1': value1,
        'value2': value2,
        'value3': value3,
    }

    result = requests.post(url2, json=data, headers=hed)
    return result.json()

def verifySpPayment(order_id):
    # url = 'https://sandbox.shurjopayment.com/api/get_token'
    # url2 = 'https://sandbox.shurjopayment.com/api/verification'
    # access = {
    #     "username":"sp_sandbox",
    #     "password":"pyyk97hu&6u6"
    # }
    url = 'https://engine.shurjopayment.com/api/get_token'
    url2 = 'https://engine.shurjopayment.com/api/verification'
    access = {
        "username":"lyriczsoft",
        "password":"lyrikskdzprvz&ud"
    }
    result  = requests.post(url, data=access)
    result = result.json()
    token = result['token']
    store_id = result['store_id']
    execute_url = result['execute_url']
    hed = {'Authorization': 'Bearer ' + token}

    data = {
        "order_id": order_id,
    }
    result = requests.post(url2, data=data, headers=hed)
    res = result.json()
    return res[0]