from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .viewsCardinals import CordenadaListCreateView,CordenadasUpdateView,CordenadasDeleteView,CordenadasDetailView,AllCordenadasListView
from .viewsProvider import ProveedorDeleteView,ProveedorDetailView,ProveedorListCreateView,ProveedorUpdateView,AllProveedoresListView
from .viewsUser import  CreateUser, UpdateUser, GetAllUser, DeleteUser
from .viewsRols import RolListCreateView, RolDetailView, RolDeleteView, RolUpdateView, AllRolListView

urlpatterns = [
    #proveedores
    path('proveedor/', ProveedorListCreateView.as_view(), name='proveedor-list-create'),
    path('proveedor/<int:pk>', ProveedorDetailView.as_view(), name='proveedor-detail'),
    path('proveedor/all/', AllProveedoresListView.as_view(), name='all-proveedor-list'),
    path('proveedor/delete/<int:pk>', ProveedorDeleteView.as_view(), name='proveedor-delete'),
    path('proveedor/update/<int:pk>', ProveedorUpdateView.as_view(), name='proveedor-update'),
    #cordenadas
    path('cordenadas/', CordenadaListCreateView.as_view(), name='cordenadas-list-create'),
    path('cordenadas/<int:pk>', CordenadasDetailView.as_view(), name='cordenadas-detail'),
    path('cordenadas/all/', AllCordenadasListView.as_view(), name='all-cordenadas-list'),
    path('cordenadas/delete/<int:pk>', CordenadasDeleteView.as_view(), name='cordenadas-delete'),
    path('cordenadas/update/<int:pk>', CordenadasUpdateView.as_view(), name='cordenadas-update'),
    #token
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    #user
    path('user/', CreateUser.as_view(), name='create-user'),
    path('user/update/', UpdateUser.as_view(), name='update-user'),
    path('user/all/', GetAllUser.as_view(), name='get-all-user'),
    path('user/delete/', DeleteUser.as_view(), name='delete-user'),
    #rol
    path('rol/',RolListCreateView.as_view(), name='rol-create'), 
    path('rol/all/', AllRolListView.as_view(), name='all-rol-list'),
    path('rol/delete/<int:pk>', RolDeleteView.as_view(), name='rol-delete'),
    path('rol/update/<int:pk>', RolUpdateView.as_view(), name='rol-update'),
    path('rol/<int:pk>', RolDetailView.as_view(), name='rol-detail')
]

