from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import JsonResponse


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