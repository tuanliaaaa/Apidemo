from  News.settings import key
import jwt
class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self, request):   
        if 'Authorization' in request.headers:
            jwtTokenSplit=request.headers['Authorization'].split(' ')
            jwtTokenpayload = jwtTokenSplit[1]
            PayLoad=jwt.decode(jwtTokenpayload, key, algorithms=["HS256"])
            request.groupNames=PayLoad['Group']
        response = self.get_response(request)
        return response