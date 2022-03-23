from audioop import reverse
from django.core.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.response import Response
def RoleRequest(allowedRoles=[]):
    def decorator(ViewFuntion):
        def wrap(request,*args,**kwargs):
            CheckAuthoration = False
            for allowedRole in allowedRoles:
                if allowedRole in request.groupNames:
                    CheckAuthoration = True
                    return ViewFuntion(request,*args,**kwargs)
            if not CheckAuthoration:
                return Response({"message":"bạn không có quyền truy cập"},status=status.HTTP_403_FORBIDDEN)
        return wrap
    return decorator