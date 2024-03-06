from django.urls import path
from .views import ProveedorDeleteView,ProveedorDetailView,ProveedorListCreateView,ProveedorUpdateView,AllProveedoresListView,CordenadaListCreateView,CordenadasUpdateView,CordenadasDeleteView,CordenadasDetailView,AllCordenadasListView, CreateUser, UpdateUser, GetAllUser, DeleteUser
from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('proveedor/', ProveedorListCreateView.as_view(), name='proveedor-list-create'),
    path('proveedor/<int:pk>', ProveedorDetailView.as_view(), name='proveedor-detail'),
    path('proveedor/all/', AllProveedoresListView.as_view(), name='all-proveedor-list'),
    path('proveedor/delete/<int:pk>', ProveedorDeleteView.as_view(), name='proveedor-delete'),
    path('proveedor/update/<int:pk>', ProveedorUpdateView.as_view(), name='proveedor-update'),
    path('cordenadas/', CordenadaListCreateView.as_view(), name='cordenadas-list-create'),
    path('cordenadas/<int:pk>', CordenadasDetailView.as_view(), name='cordenadas-detail'),
    path('cordenadas/all/', AllCordenadasListView.as_view(), name='all-cordenadas-list'),
    path('cordenadas/delete/<int:pk>', CordenadasDeleteView.as_view(), name='cordenadas-delete'),
    path('cordenadas/update/<int:pk>', CordenadasUpdateView.as_view(), name='cordenadas-update'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', CreateUser.as_view(), name='create-user'),
    path('user/update/', UpdateUser.as_view(), name='update-user'),
    path('user/all/', GetAllUser.as_view(), name='get-all-user'),
    path('user/delete/', DeleteUser.as_view(), name='delete-user')
]

