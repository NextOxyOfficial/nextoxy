from django.shortcuts import render
from datetime import datetime
from core.mailing import send_mail
from django.http import HttpResponse
from pathlib import Path
import os
from django.template import engines
import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response

message = '''
<p>Hi there23423,</p>
<p>Sometimes you just want to send a simple HTML email with a simple design and clear call to action. This is it.</p>
<table role="presentation" border="0" cellpadding="0" cellspacing="0" class="btn btn-primary">
  <tbody>
    <tr>
      <td align="left">
        <table role="presentation" border="0" cellpadding="0" cellspacing="0">
          <tbody>
            <tr>
              <td> <a href="http://htmlemail.io" target="_blank">Click me</a> </td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
  </tbody>
</table>
<p>This is a really simple email template. Its sole purpose is to get the recipient to click the button with no distractions.</p>
<p>Good luck! Hope it works.3254345</p>
'''

def index(request, **args):
    print('start', datetime.now())
    # send_mail('subject', message, ['shimul929@gmail.com'])
    print('end', datetime.now())
    return render(request, 'index.html')

def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
     'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
     'var firebaseConfig = {' \
     '        apiKey: "AIzaSyBdG0LUHm6y1GAjhtV8w3KXJ-mLJ7-_Lm4",' \
     '        authDomain: "ajkerpristha.firebaseapp.com",' \
     '        databaseURL: "https://ajkerpristha-default-rtdb.firebaseio.com/",' \
     '        projectId: "ajkerpristha",' \
     '        storageBucket: "ajkerpristha.appspot.com",' \
     '        messagingSenderId: "398614736048",' \
     '        appId: "1:398614736048:web:c49bdeb58296508bdcdf75",' \
     '        measurementId: "VWZMRP7HEV"' \
     ' };' \
     'firebase.initializeApp(firebaseConfig);' \
     'const messaging=firebase.messaging();' \
     'messaging.setBackgroundMessageHandler(function (payload) {' \
     '    console.log(payload);' \
     '    const notification=JSON.parse(payload);' \
     '    const notificationOption={' \
     '        body:notification.body,' \
     '        icon:notification.icon' \
     '    };' \
     '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
     '});'

    return HttpResponse(data,content_type="text/javascript")

def render_template_from_url(request, url, context={}):
    # Fetch the template content from the URL
    if request.build_absolute_uri('/')[:-1] == 'http://127.0.0.1:8000':
      baseURL = 'http://127.0.0.1:8000'
    else:
      baseURL = 'http://localhost'
    response = requests.get(baseURL+url)
    if response.status_code == 200:
        template_content = response.text
        # Assuming you're using the default Django template engine
        django_engine = engines['django']
        template = django_engine.from_string(template_content)
        # Render the template
        rendered_template = template.render(context, request=request)
        return HttpResponse(rendered_template)
    else:
        return HttpResponse("E"+str(response.status_code))

def test(request, **args):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'media'))
    url = os.path.join(MEDIA_ROOT, 'installed', 'themes', 'website', 'site1')
    random = datetime.now().strftime('%Y%m%d%H%M%S')
    with open(os.path.join(url, 'test12.html'), 'w') as f:
        f.write('hello world '+ str(random))
    return HttpResponse(url)
def test1(request, **args):
  url = '/static/templates/index.html'
  return render_template_from_url(request, url, {"test":"success"})

@api_view(['GET','POST', 'OPTIONS'])
def test2(request, **args):
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  url = os.path.abspath(os.path.join(BASE_DIR, 'static','templates','index.html'))
  random = datetime.now().strftime('%Y%m%d%H%M%S')
  content = request.GET.get('content', ' - ')
  with open(url, 'w') as f:
        f.write('hello world '+ str(random) + str(content))
  return Response(random)

