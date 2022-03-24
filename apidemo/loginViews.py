from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
class LoginAjax(View):
    
    def get(self,request):
        return render(request,'login.html')