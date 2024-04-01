from django.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from django.http import JsonResponse

class GetToken(APIView):
    def obtain_jwt_token(request):
        # Obtén el token JWT para el usuario autenticado
        token = AccessToken.for_user(request.user)

        # Agrega los roles al token 
        # falta definir los roles
        token['is_admin'] = request.user.userprofile.is_patient
        token['is_user'] = request.user.userprofile.is_medical
        token['is_provider'] = request.user.userprofile.is_physiotherapist

        # Devuelve el token como respuesta
        return JsonResponse({'token': str(token)})