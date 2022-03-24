from  News.settings import key
import jwt
from rest_framework.response import Response
from rest_framework import status
import json
from django.http.response import HttpResponse
class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):   
        if 'Authorization' in request.headers:
            jwtTokenSplit=request.headers['Authorization'].split(' ')
            jwtTokenpayload = jwtTokenSplit[1]
            try:
                PayLoad=jwt.decode(jwtTokenpayload, key, algorithms=["HS256"])
                request.groupNames=PayLoad['Group']
                request.userID=PayLoad['UserID']
               
            except:
                a=json.loads('{"message":"Token đã hết hạn"}')
                return HttpResponse(a,status =status.HTTP_403_FORBIDDEN)
        response = self.get_response(request)
        return response