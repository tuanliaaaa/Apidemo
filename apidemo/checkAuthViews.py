from  News.settings import key
import jwt
def CheckAuth(a,CheckArticles=0):
    try:
        
        jwt_payloadSplit=a['Authorization'].split(' ')
        jwt_payload = jwt_payloadSplit[1]
        jwt_payloadDecode=jwt.decode(jwt_payload, key, algorithms=["HS256"])
        if jwt_payloadDecode['Group']=="admin":
            return 1
        else:
            if(CheckArticles):
                print('vcl')
                return 1
            else:
                    return 0
    except:
        return 0
