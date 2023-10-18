from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Client
from .serializers import ClientSerializer

# Create your views here.
def authorize(request):
  params = request.GET.dict()
  authorize = Client.objects.filter(client_secret=params["client_secret"])
  authorize = authorize.filter(client_id=params["client_id"])
  authorize = authorize.filter( redirect_uri=params["redirect_uri"])
  response_types = authorize[0].response_types.all()
  serializer = ClientSerializer(authorize[0])
  print(authorize.exists(), len(authorize), response_types.filter(name=params['response_type']).exists())
  if authorize.exists() and len(authorize) == 1 and response_types.filter(name=params['response_type']).exists():
    return JsonResponse(serializer.data, safe=False, status=200)
  else:
    return JsonResponse({"error": "invalid_request"}, status=400)

def index(request):
  return HttpResponse("Hello, world. You're at the oauth_server index.")    