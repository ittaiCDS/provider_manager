from rest_framework import generics
from .models import Cordenadas
from .serializers import CoordenadasSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
    

class CordenadaListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cordenadas.objects.all()
    serializer_class = CoordenadasSerializer
 
class CordenadasUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cordenadas.objects.all()
    serializer_class = CoordenadasSerializer
    partial = True
    
class CordenadasDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cordenadas.objects.all()
    serializer_class = CoordenadasSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("Delete Coordenadas"))

class CordenadasDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cordenadas.objects.all()
    serializer_class = CoordenadasSerializer

class AllCordenadasListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cordenadas.objects.all()
    serializer_class = CoordenadasSerializer
   
