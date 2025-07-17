from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def get_question(request):
    print(f"METHOD: {request.method}") 
    if request.method == 'GET':
        data = {
            "id": 1,
            "text": "ประเทศไทยมีกี่จังหวัด",
            "choices": [50, 68, 72, 77]
        }
        return JsonResponse(data)
    
@csrf_exempt
def create_question(request):
    print(f"METHOD: {request.method}") 
    if request.method == 'POST':
        body = json.loads(request.body)
        return JsonResponse(body, status=201)