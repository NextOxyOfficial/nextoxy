from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import openai

@api_view(['GET', 'DELETE','POST', 'PUT'])
def ai(request):
    openai.organization = "org-mKA4ISUauJg2LpBXfDpXzMjO"
    openai.api_key = "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"
    # print(openai.Model.list())
    response = ''
    prompt = request.GET.get('prompt', None)
    if prompt:
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
        response = completion.choices[0].message.content
    return Response(response)
