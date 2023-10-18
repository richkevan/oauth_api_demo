from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Client
from .serializers import ClientSerializer

# Create your views here.
def authorize(request):
  params = request.GET.dict()
  authorize = Client.objects.get(client_secret=params["client_secret"], client_id=params["client_id"], redirect_uri=params["redirect_uri"])
  scopes = authorize.scope.all()
  response_types = authorize.response_types.all()
  grant_types = authorize.grant_types.all()
  serializer = ClientSerializer(authorize)
  if authorize.DoesNotExist:
    return JsonResponse({"error": "invalid_request"}, status=400)
  else:
    return JsonResponse(serializer.data, safe=False, status=200)

def index(request):
  return HttpResponse("Hello, world. You're at the oauth_server index.")    