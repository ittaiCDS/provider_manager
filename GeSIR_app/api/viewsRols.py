from rest_framework import generics
from .models import Rol, Usuario_Rol
from .serializers import RolSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from datetime import datetime



class CreateRol(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, * args, **kwargs):
        codigo = request.data['codigo']
        nombre = request.data['nombre']
        descripcion = request.data['descripcion']
        estatus = True
        creacion = datetime.now()
        actualizacion = datetime.now()
        
        data = {
            "codigo" : codigo,
            "nombre" : nombre,
            'descripcion' : descripcion,
            'estatus' : estatus,
            'creacion' : creacion,
            'actualizacion' :actualizacion
        }
        Rol.objects.create_rol(
            codigo=codigo, 
            nombre=nombre,
            descripcion=descripcion,
            estatus=estatus,
            creacion=creacion,
            actualizacion=actualizacion
        )
        return JsonResponse({"datos" : data})
    
class GetAllRol(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        queryset = Rol.objects.all()
        rols = RolSerializer(queryset, many=True).data
        return JsonResponse({"datps":rols})
    
class UpdateRol(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, *args, **kwargs):
        codigo = request.data['codigo']
        nombre = request.data['nombre']
        descripcion = request.data['descripcion']
        actualizacion = datetime.now()
        rol = Rol.objects.get(codigo=codigo)
        rol.nombre = nombre
        rol.descripcion = descripcion
        rol.actualizacion = actualizacion
        rol.save()
        return JsonResponse({"datos" : rol})

class DeleteRol(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        codigo = request.data['codigo']
        rol = Rol.objects.get(codigo = codigo)
        rol.estatus = False
        rol.save()
        return JsonResponse({"datos" : rol})

'''class RolListCreateView(generics.ListCreateAPIView):
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
'''