from rest_framework.decorators import APIView
from rest_framework.response import Response
from api.threads import SendEmailtoUser
import re 

# from api.helpers import send_email_to

# Create your views here.

def home(request):
    return(request,'email_template.html')

# Provide Username and Send_to fields in Postman as JSON
#like this 
# {
#     "username":"SAHIL HUSSAIN",
#     "send_to":"srhussain.sr@gmail.com"
# }
class sendemail(APIView):
    def post(self,request):
        try:
            data=request.data
            username=data.get('username')
            send_to=data.get('send_to')
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if not (re.fullmatch(regex, send_to)):
                    return Response({
                'status':404,
                'message':"Please Enter Valid Email ID !"
                    })
            SendEmailtoUser(send_to,username).start()
            return Response({
                'status':200,
                'message':f"Email Sent to {username} Successfully !"
            })
        except Exception as e:
            print(e)
        return Response({
            'message':'Something went wrong'
        })
        
