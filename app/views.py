from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

#this is the function based view
@api_view(['GET','POST'])
def  get_data(request):
    if request.method=='GET':
        return Response({"message":"get the data"})
    if request.method == 'POST':
        return Response({"message":"post the data"})

class protected_view(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({"message":"you are authenticated"})


