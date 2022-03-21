from django.http import JsonResponse
from django.shortcuts import render
import json

# Create your views here.
from django.views import View

class UserViews(View):
    # def get(self,request):
    #     return JsonResponse({"code":100})
    def post(self,request):
        json_str = request.body
        json_obj = json.loads(json_str)
        username = json_obj['username']
        email = json_obj['email']
        phone = json_obj['phone']
        password_1 = json_obj['password_1']
        password_2 = json_obj['password_2']



        result = {'code':200}
        return JsonResponse(result)