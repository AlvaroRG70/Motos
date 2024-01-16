from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import *

@api_view(['GET'])
def moto_list(request):
    
    motos = Moto.objects.all()
    serializer = UsuarioSerializer(motos, many=True)
    return Response(serializer.data)