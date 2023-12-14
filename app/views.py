from .models import User

from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

from json import loads, JSONDecodeError

# Create your views here.
def get_users(request: HttpRequest):
    if (request.method != 'GET'):
        return HttpResponseBadRequest("Esta visualização só aceita métodos GET")
    return JsonResponse({'objects': [user.__json__() for user in User.objects.all()]})

@csrf_exempt
def post_user(request: HttpRequest):
    if (request.method != 'POST'):
        return HttpResponseBadRequest("Esta visualização só aceita métodos POST")
    try:
        data = loads(request.body.decode('utf-8'))
        User.objects.create(name=data['name'], password=data['password'])
        return JsonResponse({'object': data})
    except JSONDecodeError:
        return JsonResponse({'error': 'Erro ao decodificar o JSON'})
    