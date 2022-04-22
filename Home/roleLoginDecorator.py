from audioop import reverse
from django.core.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response
from django.http.response import HttpResponseRedirect

def RoleLogin(ViewFuntion):
    def wrap(request,*args,**kwargs):
        try:
            if request.groupNames:
                return ViewFuntion(request,*args,**kwargs)
        except:
            return HttpResponseRedirect('/login/')
    return wrap
    
