
from .notif_fb import push
from .notif_mail import send

data = {
  1: {
    'title': 'Welcome to NextOxy.',
    'text': 'Dear [name], Congratulations! Your registration with NextOxy has been successfully completed, and we are thrilled to welcome you to our community.',
    'html': '''
    <p>Dear [name],</p>
    <p>Congratulations! Your registration with NextOxy has been successfully completed, and we are thrilled to welcome you to our community.</p>
    <ul>
      <li>If you have any questions or encounter any issues with your account, feel free to reach out to our customer support team at support@nextoxy.com. We're here to assist you.</li>
    </ul>
    <p>Warm Regards,</p>
    '''
  },
  2: {
    'title': 'Order Received Confirmation.',
    'text': 'Dear [name], We are delighted to inform you that we have successfully received your order. Our team is now processing your order. We appreciate your business and look forward to serving you.',
    'html': '''
    <p>Dear [name],</p>
    <p>We are delighted to inform you that we have successfully received your order. Our team is now processing your order. We appreciate your business and look forward to serving you.</p>
    <ul>
      <li>If you have any questions or encounter any issues with your account, feel free to reach out to our customer support team at support@nextoxy.com. We're here to assist you.</li>
    </ul>
    <p>Warm Regards,</p>
    '''
  },
  3: {
    'title': 'Your Shop Received A New Order.',
    'text': 'Dear [name], Exciting news! A new order has just been placed on your shop.  Please begin processing the order promptly to ensure a timely dispatch. The customer is eagerly anticipating their purchase. ',
    'html': '''
    <p>Dear [name],</p>
    <p>Exciting news! A new order has just been placed on your shop.  Please begin processing the order promptly to ensure a timely dispatch. The customer is eagerly anticipating their purchase. </p>
    <ul>
      <li>If you have any questions or encounter any issues with your account, feel free to reach out to our customer support team at support@nextoxy.com. We're here to assist you.</li>
    </ul>
    <p>Warm Regards,</p>
    '''
  },
  4: {
    'title': 'New Message Received - Customer Support.',
    'text': 'Dear [name], You have received a new message! To view and respond to the message, please proceed to the Customer Support Desk.',
    'html': '''
    <p>Dear [name],</p>
    <p>You've received a new message! To view and respond to the message, please proceed to the Customer Support Desk.</p>
    <ul>
      <li>If you have any questions or encounter any issues with your account, feel free to reach out to our customer support team at support@nextoxy.com. We're here to assist you.</li>
    </ul>
    <p>Warm Regards,</p>
    '''
  },
}



def notify(member, other, amount, mid):
    tokens = member.fb_tokens
    email = member.email
    message = data[mid]
    if member.first_name and member.last_name:
      name = member.first_name = ' '+ member.last_name
    else:
       name = ''
    message['text'] = message['text'].replace('[name]', name)
    message['html'] = message['html'].replace('[name]', name)

    if other:
        message['text'] = message['text'].replace('[o_name]', name)
        message['html'] = message['html'].replace('[o_name]', name)
    if amount:
        message['text'] = message['text'].replace('[amount]', str(amount))
        message['html'] = message['html'].replace('[amount]', str(amount))
    print(member, member.email, tokens, 444)
    try:
      push(tokens, message)
    except Exception as e:
      print('Push Notification Failed!', e)
    
    try:
      send(email, message)
    except Exception as e:
      print('Email Sending Failed!', e)

    