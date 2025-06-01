from django.contrib.auth.models import User
from affiliate.models import Affiliate
from rest_framework import serializers
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
import time
import random
import string
from core.models import Account, Notification, Ticket, TicketMessage
from core.mailing import send_mail
from core.mail_templates import registration_message, password_reset_message, password_updated_message
from core.utils import strToFile


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
class TicketSerializer(serializers.ModelSerializer):
    message_count = serializers.SerializerMethodField()
    class Meta:
        model = Ticket
        fields = '__all__'
    def get_message_count(self, obj):
        return obj.ticketmessage_set.count()
class TicketMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketMessage
        fields = '__all__'

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.username
        return token

@api_view(['GET','POST', 'OPTIONS'])
def loginUser(request):
    user = request.user
    data = None
    if request.method == 'POST':
        username = request.data.get('identity')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
    if user is not None and user.account:
        data = AccountSerializer(user.account).data
        data['jwt'] = str( MyTokenObtainPairSerializer.get_token(user).access_token )
        data['notifications'] = Notification.objects.filter(account=user.account, unread=True ).count()
    return Response(data)

@api_view(['GET','POST', 'OPTIONS'])
@permission_classes([AllowAny])
def notifications(request):
    account = Account.objects.get(id=request.GET.get('acc_id'))
    qs = Notification.objects.filter(account=account).order_by('-unread','-created_at')[:6]
    data = NotificationSerializer(qs, many=True).data
    Notification.objects.filter(account=account, unread=True ).update(unread=False)
    return Response(data)

@api_view(['GET','POST', 'OPTIONS'])
def tickets(request):
    user = request.user
    if request.method == 'POST':
        data = request.data
        if 'subject' in data and 'message' in data:
            tc = Ticket.objects.create(subject=data['subject'], account=user.account)
            tm = TicketMessage.objects.create(ticket = tc, content=data['message'])
            if 'image' in data and len(data['image']) > 10:
                tm.image = strToFile(data['image'])
                tm.save()
            # Notification.objects.create(type="order", content="New support ticket opened", account=user.account)
            # send_mail('New ticket opened', new_ticket_message, [user.account.email])
        if 'tid' in data and 'message' in data:
            tc = Ticket.objects.get(id=data['tid'])
            tm = TicketMessage.objects.create(ticket = tc, content=data['message'])
            if 'image' in data and len(data['image']) > 10:
                tm.image = strToFile(data['image'])
                tm.save()
    tid = request.GET.get('tid', None)
    if tid:
        tc = Ticket.objects.get(id=tid)
        qs = TicketMessage.objects.filter(ticket=tc)
        data = TicketMessageSerializer(qs, many=True).data
        return Response(data)
    qs = Ticket.objects.filter(account = user.account).order_by('-id')
    data = TicketSerializer(qs, many=True).data
    return Response(data)




@api_view(['POST'])
@permission_classes([AllowAny])
def registerUser(request):
    if request.method == 'POST':
        data = request.data
        if User.objects.filter(email=data['email']).exists():
            return Response('User with this email already exists')
        new_user = User (
            username = data['email'],
            email = data['email'],
        )
        new_user.set_password(data['password'])
        new_user.save()
        new_account = Account (
            user = new_user,
            email = data['email'],
        )
        new_account.save()
        if 'refer' in data and data['refer']:
            if Affiliate.objects.filter(affiliate_code=data['refer']).exists():
                affiliate = Affiliate.objects.get(affiliate_code=data['refer'])
                affiliate.registrations = affiliate.registrations + 1
                affiliate.save()
                new_account.affiliate = affiliate
                new_account.save()
        send_mail('Registration successful!', registration_message, [new_account.email])
            
        return Response(200)



@api_view(['POST', 'GET'])
def resetUser(request):
    email = request.GET.get('email', None)
    otp = request.GET.get('otp', None)
    if request.method =='POST':
        data = request.data
        otp = data['otp']
        if Account.objects.filter(otp=otp).exists():
            password = data['pass1']
            user = Account.objects.get(otp=otp).user
            user.set_password(password)
            user.save()
            Notification.objects.create(type="other", content="Your password has been updated!", account=user.account)
            send_mail('Password updated!', password_updated_message, [user.account.email])
            return Response(200)
        else:
            return Response(404)
    if otp:
        if Account.objects.filter(otp=otp).exists():
            return Response(200)
        else:
            return Response(404)
    if email:
        email = email.strip()
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=30))
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            user.account.otp = random_string
            user.account.save()
            reset_message2 = password_reset_message.replace('[link]', 'https://nextoxy.com/auth/reset?otp=' + random_string)
            send_mail('Reset Password!', reset_message2, [email])
        else:
          return Response(404)
    return Response(200)