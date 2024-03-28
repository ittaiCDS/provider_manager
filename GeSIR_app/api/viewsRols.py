from rest_framework import generics
from .models import Rol, Usuario_Rol
from .serializers import RolSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class RolListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    
class RolUpdateView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    partial = True
    
   
class RolDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("Delete Rol"))

class RolDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Rol.objects.all()
    serializer_class = RolSerializer


class AllRolListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
