from django.shortcuts import render

from django.views.generic import View
from django.http import JsonResponse

from json import loads

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from app.models import Player
# Create your views here.

@method_decorator(csrf_exempt,name="dispatch")
class PlayerListCreateView(View):
    def get(self,request):
        qs = Player.objects.all().values()
        response_data = list(qs)
        return JsonResponse(response_data,safe=False)
    
    def post(self,request):
        json_data = request.body
        form_data = loads(json_data)
        """
        {
            "name":"messi",
            "age":39,
            "sport":"football",
            "role":"stricker",
            "country":"argentina"
        }
        """
        Player.objects.create(**form_data)
        
        response_data = {"message":"player created ...."}
        return JsonResponse(response_data)
        
    
@method_decorator(csrf_exempt,name="dispatch")
class PlayerRetrieveUpdateDeleteView(View):
    def get(self,request,pk=None):
        qs = Player.objects.filter(id=pk).values()
        response_data = list(qs)
        return JsonResponse(response_data,safe=False)
    
    def put(self,request,pk=None):
        json_data = request.body
        form_data = loads(json_data)
        Player.objects.filter(id=pk).update(**form_data)
        response_data = {"message":"player updated ...."}
        return JsonResponse(response_data)
    
    def delete(self,request,pk=None):
        Player.objects.filter(id=pk).delete()
        response_data = {"message":"player deleted ...."}
        return JsonResponse(response_data)

