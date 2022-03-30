from audioop import reverse
from django.core.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response
from django.http.response import HttpResponseRedirect
def RoleRequest(allowedRoles=[]):
    def decorator(ViewFuntion):
        def wrap(request,*args,**kwargs):
            checkAuthorization = False
            for allowedRole in allowedRoles:
                if allowedRole in request.groupNames:
                    checkAuthorization = True
                    return ViewFuntion(request,*args,**kwargs)
            if not checkAuthorization:
                return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_403_FORBIDDEN)
        return wrap
    return decorator