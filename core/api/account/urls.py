from django.urls import path
from .views import *
urlpatterns = [
    path('ecommerce/', ecommerce), #user's shop
    path('business/', business), #user's business
    path('eblog/', eblog), #user's blog
    path('website/', website), #user's blog
    path('blog/', blog), # nextoxy blog post
    path('blog_categories/', blog_category), # nextoxy blog post
    path('mediafiles', MediaFiles),
    path('profile', profile),
    path('password', password),
    path('invoices', invoices),
    path('paypal/pay/<int:id>', paypalPay), # stripe
    path('stripe/pay/<int:id>', stripePay), # stripe
    path('stripe/verify', stripeVerify), #stripe verify webhook
    path('sp/pay/<int:id>', spPay), # sp and verify
    # service order 
    path('service', service),
    path('domains', domains),
    path('fb_tokens/', fb_tokens),
]