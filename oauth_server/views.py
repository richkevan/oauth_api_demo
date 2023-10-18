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
  html = """
  <html>
    <body>
      <a href='/authorize/?client_secret=rTIC2rpywxewS0R75XwwIXIatTeCyXRi&client_id=Demo&redirect_uri=demo.com%2Fcallback&response_type=code' target='_blank'>try authorizing a valid client</a>
      <br>
      <a href='/authorize/?client_secret=rTIC2rpywxewS0R75XwwIXIatTeCyXRi&client_id=Demo&redirect_uri=demo.com%2Fcallback&response_type=request' target='_blank'>try authorizing an invalid client</a>
    </body>
  </html>
  """
  return HttpResponse(html)    