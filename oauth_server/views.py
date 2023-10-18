from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Client
from .serializers import ClientSerializer

# Create your views here.
def authorize(request):
  params = request.GET.dict()
  authorize = Client.objects.get(client_secret=params["client_secret"])
  authorize = authorize.filter(client_id=params["client_id"])
  authorize = authorize.filter( redirect_uri=params["redirect_uri"])
  response_types = authorize.response_types.all()
  serializer = ClientSerializer(authorize)
  if authorize & params["response_type"] in response_types:
    return JsonResponse(serializer.data, safe=False, status=200)
  else:
    return JsonResponse({"error": "invalid_request"}, status=400)

def index(request):
  return HttpResponse("Hello, world. You're at the oauth_server index.")    