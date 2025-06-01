from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import os
from django.template import engines
from django.http import HttpResponse
from .models import *
# Create your views here.

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


def test1(request, **args):
  url = '/static/templates/index.html'
  blocks = Block.objects.all()
  return render_template_from_url(request, url, {"test":"success", "blocks":blocks})

@api_view(['GET','POST', 'OPTIONS'])
def test2(request, **args):
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  url = os.path.abspath(os.path.join(BASE_DIR, 'static','templates','index.html'))
  random = datetime.now().strftime('%Y%m%d%H%M%S')
  content = request.GET.get('content', ' - ')
  with open(url, 'w') as f:
        f.write('hello world '+ str(random) + str(content))
  return Response(random)