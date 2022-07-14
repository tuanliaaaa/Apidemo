from django.shortcuts import render
from django.views import View

from django.utils.decorators import method_decorator
from django.http.response import HttpResponseRedirect
from audioop import reverse
# Create your views here.
class Home(View):
    def get(self,request):
        
        return render(request,'home.html',)
