# from buy.serializers import buySerializers
from buy.models import txtmodel
# from rest_framework.generics import ListAPIView
# from rest_framework.permissions import AllowAny
from pathlib import Path
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

# class txtmodelListAPIView(ListAPIView):
 

#     def get_queryset(self):
#         BASE_DIR = Path(__file__).resolve().parent.parent
#         a = txtmodel.objects.first()
#         aa = a.filetxt
#         f = open(str(BASE_DIR) +"/"+ str(aa), "r")
#         # print(f.read())
#         return str(f.read())
        
#     serializer_class = buySerializers
#     permission_classes = [AllowAny]
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def pay(request):
    BASE_DIR = Path(__file__).resolve().parent.parent
    a = txtmodel.objects.first()
    aa = a.filetxt
    f = open(str(BASE_DIR) +"/"+ str(aa), "r")
    return Response(str(f.read()))