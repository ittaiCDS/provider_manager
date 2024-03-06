from rest_framework import generics, status
from .models import Proveedor, Cordenadas
from .serializers import ProveedorSerializer, CoordenadasSerializer, UserSerializer
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import JsonResponse

class ProveedorListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
 
class ProveedorUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    partial = True
    
class ProveedorDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("Delete Proveedor"))

class ProveedorDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer


class AllProveedoresListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Proveedor.objects.all()
    serializer_class = CoordenadasSerializer
    

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
   
class CreateUser(APIView):  
    permission_classes = [IsAuthenticated]  
    def post(self, request, *args, **kwargs):
        userName = request.data['username']
        userPass = request.data['password']
        data = {"user" : userName, "pass" : userPass}
        User.objects.create_user(username=userName, password=userPass)
        return JsonResponse({"datos" :  data})
    
class GetAllUser(APIView):
    parser_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        queryset = User.objects.all()
        users = UserSerializer(queryset, many=True).data
        return JsonResponse({"datos" :  users})

class UpdateUser(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, *args, **kwargs):
        userName_old = request.data['username_old']
        userName = request.data['username']
        userPass = request.data['password']
        data = {"user" : userName, "pass" : userPass}
        user = User.objects.get(username = userName_old)
        user.username = userName
        user.password = userPass
        user.save()
        return JsonResponse({"datos" :  data})
    
class DeleteUser(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        userName = request.data['username']
        data = {"user" : userName}
        user = User.objects.get(username = userName)
        estatus_set = False  if user.is_active == True  else True 
        print(estatus_set)
        user.is_active = estatus_set
        user.save()
        return JsonResponse({"datos" :  data})