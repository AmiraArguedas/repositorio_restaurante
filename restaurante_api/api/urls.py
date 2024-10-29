from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # url de ROLES
    path('roles/', views.RolesListCreate.as_view(), name='roles-list'), 
    path('roles/<int:pk>/', views.RolesDetail.as_view(), name='roles-detail'), 
    
    
    # url de USUARIO
    path('usuarios/', views.UsuarioListCreate.as_view(), name='usuarios-list'), 
    path('usuarios/<int:pk>/', views.UsuarioDetail.as_view(), name='usuarios-detail'), 
   
   
    # url de MENU
    path('menu/', views.MenuListCreate.as_view(), name='menu-list'), 
    path('menu/<int:pk>/', views.MenuDetail.as_view(), name='menu-detail'), 
   
   
    # url de HISTORIAL ESTADOS
    path('historialestados/', views.HistorialEstadosListCreate.as_view(), name='historialestados-list'), 
    path('historialestados/<int:pk>/', views.HistorialEstadosDetail.as_view(), name='historialestados-detail'), 
   
   
    # url de PEDIDOS
    path('pedidos/', views.PedidoListCreate.as_view(), name='pedidos-list'), 
    path('pedidos/<int:pk>/', views.PedidoDetail.as_view(), name='pedidos-detail'), 
  
  
    # url de PROMOCIONES
    path('promociones/', views.PromocionListCreate.as_view(), name='promociones-list'), 
    path('promociones/<int:pk>/', views.PromocionDetail.as_view(), name='promociones-detail'), 
  
  
    # url de DETALLES PEDIDOS
    path('detallepedidos/', views.DetallePedidoListCreate.as_view(), name='detallepedidos-list'), 
    path('detallepedidos/<int:pk>/', views.DetallePedidoDetail.as_view(), name='detallepedidos-detail'),
  
  
    # url de CATEGORIA MENU
    path('categoriamenu/', views.CategoriaMenuListCreate.as_view(), name='categoriamenu-list'), 
    path('categoriamenu/<int:pk>/', views.CategoriaMenuDetail.as_view(), name='categoriamenu-detail'),
 
 
    # url de METODO DE PAGO
    path('metodosdepago/', views.MetodoDePagoListCreate.as_view(), name='metodosdepago-list'),
    path('metodosdepago/<int:pk>/', views.MetodoDePagoDetail.as_view(), name='metodosdepago-detail'),
 
 
    # url de ESTADO DE MESAS
    path('estadomesas/', views.MesasEstadoListCreate.as_view(), name='estadomesas-list'),
    path('estadomesas/<int:pk>/', views.MesasEstadoDetail.as_view(), name='estadomesas-detail'),
  
  
    # url de MESAS
    path('mesas/', views.MesasListCreate.as_view(), name='mesas-list'),
    path('mesas/<int:pk>/', views.MesasDetail.as_view(), name='mesas-detail'),
  
  
    # url de RESERVAS
    path('reservas/', views.ReservaListCreate.as_view(), name='reservas-list'),
    path('reservas/<int:pk>/', views.ReservaDetail.as_view(), name='reservas-detail'),
 
 
    # url de NOTIFICACIONES
    path('notificaciones/', views.NotificacionesListCreate.as_view(), name='producto-list'),
    path('notificaciones/<int:pk>/', views.NotificacionesDetail.as_view(), name='producto-detail'),


    # url de COMENTARIOS
    path('comentarios/', views.ComentariosListCreate.as_view(), name='producto-list'),
    path('comentarios/<int:pk>/', views.ComentariosDetail.as_view(), name='producto-detail'),


    # url de FACTURA
    path('facturas/', views.FacturaListCreate.as_view(), name='producto-list'),
    path('facturas/<int:pk>/', views.FacturaDetail.as_view(), name='producto-detail'),

    # url de usuario con sus pedidos relacionados
    path('usuarios/pedidos/<int:usuario_id>/', views.PedidoPorUsuario.as_view(), name='pedidos-por-usuario'),

    # url de usuario con sus comentarios relacionados
    path('usuarios/comentarios/<int:usuario_id>/', views.ComentarioPorUsuario.as_view(), name='comentarios-por-usuario'),

]